# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class ReadTemplate with attribute(s) and method(s).
     Read a templates and return a string representations.
'''

import sys
from os.path import isdir, exists

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(object):
    '''
        Define class ReadTemplate with attribute(s) and method(s).
        Read a templates and return a string representations.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __TEMPLATE_DIR - Prefix path to templates.
                | __template_dir - Absolute template dir.
            :methods:
                | __init__ - Initial constructor.
                | get_template_dir - Get template dir path.
                | read - Read a templates and return a content with status.
    '''

    __slots__ = ('VERBOSE', '__TEMPLATE_DIR', '__template_dir')
    VERBOSE = 'GEN_PY_TOOL::PRO::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Setting template configuration directory.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(ReadTemplate.VERBOSE, verbose, 'init reader')
        current_dir = Path(__file__).parent
        template_dir = '{0}{1}'.format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template dir path.

            :return: Template dir path | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__template_dir

    def read(self, template_modules, verbose=False):
        '''
            Read a templates and return a content with status.

            :param template_modules: Dict with template modules.
            :type template_modules: <dict>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: List of templates and True | empty list and False.
            :rtype: <list> <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('dict:template_modules', template_modules)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(ReadTemplate.VERBOSE, verbose, 'load templates')
        modules_content, status = [], False
        tool_type_key = template_modules.keys()[0]
        verbose_message(ReadTemplate.VERBOSE, verbose, tool_type_key, 'type')
        expected_num_of_modules = len(template_modules[tool_type_key])
        if self.__template_dir is not None:
            for template_module in template_modules[tool_type_key]:
                template_path = '{0}{1}/{2}'.format(
                    self.__template_dir, tool_type_key, template_module
                )
                if exists(template_path):
                    verbose_message(
                        ReadTemplate.VERBOSE, verbose,
                        'load template', template_path
                    )
                    with open(template_path, 'r') as template_file:
                        modules_content.append(template_file.read())
                else:
                    error_message(
                        ReadTemplate.VERBOSE, 'failed to load template',
                        template_path
                    )
            if len(modules_content) == expected_num_of_modules:
                status = True
        return modules_content, status
