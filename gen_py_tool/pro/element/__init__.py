# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class ElementLoader with attribute(s) and method(s).
     Created API for element checking and loding.
'''

import sys
from time import strftime

try:
    from pathlib import Path
    from gen_py_tool.pro.element.element_container import ElementContainer
    from gen_py_tool.pro.element.element_keys import ElementKeys
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
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


class ElementLoader(FileChecking, ElementContainer, ElementKeys):
    '''
        Defined class ElementLoader with attribute(s) and method(s).
        Created API for element checking and loding.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONF_DIR - configuration directory.
            :methods:
                | __init__ - initial constructor.
                | check_root_key - check root key for element.
                | process_element - process element object.
                | __str__ - dunder method for ElementLoader.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::ELEMENT::ELEMENT_LOADER'
    CONF_DIR = '/../../conf/element/'

    def __init__(self, element_file, verbose=False):
        '''
            Initial constructor.

            :param element_file: element file.
            :type element_file: <list>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:element_file', element_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        ElementContainer.__init__(self, verbose=verbose)
        verbose_message(
            ElementLoader.GEN_VERBOSE, verbose, 'init element loader'
        )
        element_path = '{0}{1}{2}'.format(
            Path(__file__).parent, ElementLoader.CONF_DIR, element_file
        )
        self.check_path(file_path=element_path, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=element_path, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(element_path)
            self.element = yml2obj.read_configuration()

    def check_root_key(self, verbose=False):
        '''
            Check root key for element.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if bool(self.element):
            for root_key in self.element.keys():
                if root_key == ElementLoader.ROOT_KEY:
                    status = True
        verbose_message(
            ElementLoader.GEN_VERBOSE, verbose, 'checking root key',
            ElementLoader.ROOT_KEY, 'defined:', status
        )
        return status

    def process_element(self, pro_name, verbose=False):
        '''
            Process element object.

            :param pro_name: project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:pro_name', pro_name)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status = False
        if self.check_root_key():
            elements = self.element[ElementLoader.ROOT_KEY]
            if isinstance(elements, list):
                statuses = []
                expected_keys = [
                    ElementLoader.TOOL_NAME_KEY, ElementLoader.TOOL_UPPER_KEY,
                    ElementLoader.TOOL_CLASS_KEY, ElementLoader.TOOL_YEAR_KEY
                ]
                for element_property, key in zip(elements, expected_keys):
                    if isinstance(element_property, dict):
                        if key in element_property:
                            if ElementLoader.TOOL_NAME_KEY == key:
                                element_property[key] = '{0}'.format(
                                    pro_name
                                )
                            if ElementLoader.TOOL_UPPER_KEY == key:
                                element_property[key] = '{0}'.format(
                                    pro_name.upper()
                                )
                            if ElementLoader.TOOL_CLASS_KEY == key:
                                element_property[key] = '{0}'.format(
                                    pro_name.capitalize()
                                )
                            if ElementLoader.TOOL_YEAR_KEY == key:
                                element_property[key] = '{0}'.format(
                                    strftime("%Y")
                                )
                            statuses.append(True)
                        else:
                            error_message(
                                ElementLoader.GEN_VERBOSE,
                                'not expected key', key
                            )
                            statuses.append(False)
                    else:
                        error_message(
                            ElementLoader.GEN_VERBOSE,
                            'element propery expected in <dict> format'
                        )
                        statuses.append(False)
                if all(statuses):
                    status = True
                else:
                    error_message(
                        ElementLoader.GEN_VERBOSE, 'failed to process element'
                    )
            else:
                error_message(
                    ElementLoader.GEN_VERBOSE,
                    'elements expected in <list> format'
                )
        else:
            error_message(ElementLoader.GEN_VERBOSE, 'element root key not ok')
        return status

    def __str__(self):
        '''
            Dunder method for ElementLoader.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ElementContainer.__str__(self)
        )
