# -*- coding: UTF-8 -*-
# format_name.py
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
from inspect import stack

try:
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


class FormatName(object):
    """
        Define class FormatName with attribute(s) and method(s).
        Generate and format file name.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                MAIN    - 0 Main module
                PROCESS - 1 Process module
                CONF    - 2 Configuration module
                __FORMAT_NAME_PY - Python filename extension
                __FORMAT_NAME_CFG - Configuration filename extension
            method:
                format_name - Formatting name for tool
                editor_config - Generating github-editor configuration
    """

    __slots__ = (
        'VERBOSE',
        'MAIN',
        'PROCESS',
        'CONF',
        '__FORMAT_NAME_PY',
        '__FORMAT_NAME_CFG'
    )
    VERBOSE = 'TOOL::FORMAT_NAME'
    MAIN, PROCESS, CONF = range(3)
    __FORMAT_NAME_PY = '.py'
    __FORMAT_NAME_CFG = '.cfg'

    @classmethod
    def format_name(cls, tool_name, module_type):
        """
            Formatting name for tool.
            :param tool_name: Tool name (translate to lower case)
            :type tool_name: <str>
            :param module_type: Type of tool (Main/Process/Configuration)
            :type module_type: <str>
            :return: File name with extension
            :rtype: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        tool_name_txt = 'Argument: expected tool_name <str> object'
        tool_name_msg = "{0} {1} {2}".format('def', func, tool_name_txt)
        module_type_txt = 'Argument: expected module_type <int> object'
        module_type_msg = "{0} {1} {2}".format('def', func, module_type_txt)
        if tool_name is None or not tool_name:
            raise ATSBadCallError(tool_name_msg)
        if not isinstance(tool_name, str):
            raise ATSTypeError(tool_name_msg)
        if module_type is None:
            raise ATSBadCallError(module_type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(module_type_msg)
        tool_name_lower = tool_name.lower()
        if module_type == FormatName.MAIN:
            tool_name_final = "{0}_run{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_PY
            )
        elif module_type == FormatName.CONF:
            tool_name_final = "{0}{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_CFG
            )
        else:
            tool_name_final = "{0}{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_PY
            )
        return tool_name_final

    @classmethod
    def editor_config(cls, file_format):
        """
            Generating content of github configuration editor.
            :param file_format: File extension
            :type file_format: <str>
            :return: Content for github editor
            :rtype: <str>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        file_format_txt = 'Argument: expected package_name <str> object'
        file_format_msg = "{0} {1} {2}".format('def', func, file_format_txt)
        if file_format is None or not file_format:
            raise ATSBadCallError(file_format_msg)
        if not isinstance(file_format, str):
            raise ATSTypeError(file_format_msg)
        editor_config = "[ **.{0}]\nindent_style = tab\ntab_width = 4".format(
            file_format
        )
        return editor_config

