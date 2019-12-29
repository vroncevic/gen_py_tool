# -*- coding: UTF-8 -*-
# write_template.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_py_tool is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_py_tool is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from os import getcwd, chmod
from os.path import exists
from datetime import date
from string import Template
from inspect import stack

try:
    from tool.format_name import FormatName

    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CHMOD - Change mode code
                __EDITOR_CONFIG - GitHub online editor configuration
                __EDITOR_CONFIG_PY - Python extension name
                __EDITOR_CONFIG_CFG - Configuration extension name
                __CLASS - Class key for template
                __FILE - File key for template
                __DATE - Date key for template
            method:
                __init__ - Initial constructor
                write - Write a template content with parameters to a file
    """

    __slots__ = (
        'VERBOSE',
        '__CHMOD',
        '__EDITOR_CONFIG',
        '__EDITOR_CONFIG_PY',
        '__EDITOR_CONFIG_CFG',
        '__CLASS',
        '__FILE',
        '__DATE'
    )
    VERBOSE = 'GEN_PY_TOOL::TOOL::WRITE_TEMPLATE'
    __CHMOD = 0666
    __EDITOR_CONFIG = '.editorconfig'
    __EDITOR_CONFIG_PY = 'py'
    __EDITOR_CONFIG_CFG = 'cfg'
    __CLASS = 'TOOL_PROCESS_CLASS'
    __FILE = 'TOOL_PROCESS_FILE'
    __DATE = 'DATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')

    def write(self, module_content, module_name, module_type):
        """
            Write a template content with parameters to a file.
            :param module_content: Template content
            :type module_content: <str>
            :param module_name: File name
            :type module_name: <str>
            :param module_type: Type of module
            :type module_type: <str>
            :return: Boolean status, True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, current_dir, func = False, getcwd(), stack()[0][3]
        mod_content_txt = 'Argument: expected module_content <str> object'
        mod_content_msg = "{0} {1} {2}".format('def', func, mod_content_txt)
        mod_name_txt = 'Argument: expected module_name <str> object'
        mod_name_msg = "{0} {1} {2}".format('def', func, mod_name_txt)
        mod_type_txt = 'Argument: expected module_type <int> object'
        mod_type_msg = "{0} {1} {2}".format('def', func, mod_type_txt)
        if module_content is None or not module_content:
            raise ATSBadCallError(mod_content_msg)
        if not isinstance(module_content, str):
            raise ATSTypeError(mod_content_msg)
        if module_name is None or not module_name:
            raise ATSBadCallError(mod_name_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(mod_name_msg)
        if module_type is None:
            raise ATSBadCallError(mod_type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(mod_type_msg)
        module_name_lower, prefix_dir = module_name.lower(), None
        github_editor, module_formatted_name = None, None
        module_file_name, today, module = None, None, None
        if module_type == FormatName.MAIN or module_type == FormatName.PROCESS:
            prefix_dir = "{0}/{1}/bin".format(current_dir, module_name_lower)
            github_editor = FormatName.editor_config(
                WriteTemplate.__EDITOR_CONFIG_PY
            )
        else:
            prefix_dir = "{0}/{1}/conf".format(current_dir, module_name_lower)
            github_editor = FormatName.editor_config(
                WriteTemplate.__EDITOR_CONFIG_CFG
            )
        module_formatted_name = FormatName.format_name(
            module_name, module_type
        )
        module_file_name = "{0}/{1}".format(prefix_dir, module_formatted_name)
        today = date.today()
        module = {
            WriteTemplate.__CLASS: "{0}".format(module_name),
            WriteTemplate.__FILE: "{0}".format(module_name_lower),
            WriteTemplate.__DATE: "{0}".format(today)
        }
        github_editor_file_path, template = None, None
        github_editor_file_path = "{0}/{1}".format(
            prefix_dir, WriteTemplate.__EDITOR_CONFIG
        )
        template = Template(module_content)
        with open(module_file_name, 'w') as module_file:
            module_content = template.substitute(module)
            module_file.write(module_content)
            github_editor_file_exists = exists(github_editor_file_path)
            if not github_editor_file_exists:
                with open(github_editor_file_path, 'w') as github_file_editor:
                    github_file_editor.write(github_editor)
                chmod(github_editor_file_path, WriteTemplate.__CHMOD)
            chmod(module_file_name, WriteTemplate.__CHMOD)
            status = True
        return True if status else False

