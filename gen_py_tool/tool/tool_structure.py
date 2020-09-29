# -*- coding: UTF-8 -*-

"""
 Module
     tool_structure.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_py_tool is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_py_tool is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class ToolStructure with attribute(s) and method(s).
     Generating tool directory structure.
"""

import sys
from inspect import stack
from os import mkdir, getcwd
from os.path import isdir

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ToolStructure(object):
    """
        Define class ToolStructure with attribute(s) and method(s).
        Generating tool directory structure.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __RUN - 0 Run directory
                | __CFG - 1 Configuration directory
                | __LOG - 2 Logging directory
                | __TOOL_SUB_STRUCTURE - Dictionary structure
            :methods:
                | gen_structure - Generating tool directory structure
    """

    __slots__ = (
        'VERBOSE',
        '__RUN',
        '__CFG',
        '__LOG',
        '__TOOL_SUB_STRUCTURE'
    )
    VERBOSE = 'GEN_PY_TOOL::TOOL::TOOL_STRUCTURE'
    __RUN, __CFG, __LOG = range(3)
    __TOOL_SUB_STRUCTURE = {
        __RUN: '/run/',
        __CFG: '/conf/',
        __LOG: '/log/'
    }

    @classmethod
    def gen_structure(cls, project_name, verbose=False):
        """
            Generating tool directory structure.

            :param project_name: Project root directory name
            :type project_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status (structure generated) True, else False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, current_dir, statuses = stack()[0][3], getcwd(), []
        project_name_txt = 'Argument: expected project_name <str> object'
        project_name_msg = "{0} {1} {2}".format('def', func, project_name_txt)
        if project_name is None or not project_name:
            raise ATSBadCallError(project_name_msg)
        if not isinstance(project_name, str):
            raise ATSTypeError(project_name_msg)
        verbose_message(ToolStructure.VERBOSE, verbose, 'Generate structure')
        project_name_lower = project_name.lower()
        root_dir = "{0}/{1}".format(current_dir, project_name_lower)
        mkdir(root_dir)
        check_root_dir = isdir(root_dir)
        statuses.append(check_root_dir)
        bin_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__RUN]
        )
        mkdir(bin_dir)
        check_bin_dir = isdir(bin_dir)
        statuses.append(check_bin_dir)
        conf_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__CFG]
        )
        mkdir(conf_dir)
        check_conf_dir = isdir(conf_dir)
        statuses.append(check_conf_dir)
        log_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__LOG]
        )
        mkdir(log_dir)
        check_log_dir = isdir(log_dir)
        statuses.append(check_log_dir)
        return all(status for status in statuses)
