# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for reading a project templates.
'''

import sys
from os.path import isdir, exists

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for reading a project templates.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - prefix path to templates.
                | __template_dir - absolute template directory.
            :methods:
                | __init__ - initial constructor.
                | get_template_dir - get template dir path.
                | read - read a templates and return a content with status.
                | __str__ - dunder method for ReadTemplate.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')
        template_dir = '{0}{1}'.format(
             Path(__file__).parent, ReadTemplate.TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def get_template_dir(self):
        '''
            Getter for template dir path.

            :return: template dir path | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__template_dir

    def read(self, template_loader, pro_type, verbose=False):
        '''
            Read a templates and return a content with status.

            :param template_loader: dict with template modules.
            :type template_loader: <dict>
            :param pro_type: project type (tool | generator).
            :type pro_type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: dict with templates and True | empty dict and False.
            :rtype: <dict> <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:template_loader', template_loader),
            ('str:pro_type', pro_type)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        template, modules_content, status = dict(), [], False
        expected_num_of_templates = len(template_loader[pro_type])
        if self.__template_dir is not None:
            for template_module in template_loader[pro_type]:
                template_path = '{0}{1}/{2}'.format(
                    self.__template_dir, pro_type, template_module
                )
                if exists(template_path):
                    verbose_message(
                        ReadTemplate.GEN_VERBOSE, verbose,
                        'load template', template_path
                    )
                    with open(template_path, 'r') as template_file:
                        modules_content.append({
                            template_module.split('.')[0]:
                            template_file.read()
                        })
                else:
                    error_message(
                        ReadTemplate.GEN_VERBOSE, 'failed to load template',
                        template_path
                    )
            if len(modules_content) == expected_num_of_templates:
                template[pro_type] = modules_content
                status = True
            else:
                error_message(
                    ReadTemplate.GEN_VERBOSE, 'failed to load all template',
                    template_path
                )
        else:
            error_message(ReadTemplate.GEN_VERBOSE, 'template dir is not ok')
        return template, status

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            self.__template_dir
        )
