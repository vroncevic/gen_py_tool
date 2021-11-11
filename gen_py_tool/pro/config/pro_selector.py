# -*- coding: UTF-8 -*-

'''
 Module
     pro_selector.py
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
     Defined class ProjectSelector with attribute(s) and method(s).
     Created API for project selector during generation process.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
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


class ProjectSelector:
    '''
        Defined class ProjectSelector with attribute(s) and method(s).
        Created API for project selector during generation process.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TYPE_KEY - project type key.
                | SCHEMA_KEY - project schema key.
                | ELEMENT_KEY - project element key.
                | TEMPLATE_KEY - project template key.
            :methods:
                | check_config_keys - checking configuration keys.
                | select_pro_type - select project type.
                | __str__ - dunder method for ProjectSelector.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::CONFIG::PROJECT_SELECTOR'
    TYPE_KEY, SCHEMA_KEY = 'types', 'schemas'
    ELEMENT_KEY, TEMPLATE_KEY = 'elements', 'templates'

    @classmethod
    def check_config_keys(cls, config, verbose=False):
        '''
            Checking configuration keys.

            :param config: dictionary with configuration.
            :type config: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (all ok) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('dict:config', config)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, expected_keys, statuses = False, [
            cls.TYPE_KEY, cls.SCHEMA_KEY, cls.ELEMENT_KEY, cls.TEMPLATE_KEY
        ], []
        for config_key in config.keys():
            if config_key in expected_keys:
                statuses.append(True)
            else:
                statuses.append(False)
        if all(statuses):
            status = True
        return status

    @classmethod
    def select_pro_type(cls, config, verbose=False):
        '''
            Select project type.

            :param config: dictionary with configuration.
            :type config: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project type and project ID | None and None.
            :rtype: <str> <int> | <NoneType> <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('dict:config', config)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        type_selected, pro_type_id = None, None
        config_ok = cls.check_config_keys(config, verbose=verbose)
        if status == ATSChecker.NO_ERROR and bool(config_ok):
            types = config[cls.TYPE_KEY]
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                print('{0} {1}'.format(index + 1, pro_type.capitalize()))
            while True:
                try:
                    try:
                        input_type = raw_input(' select project type: ')
                    except NameError:
                        input_type = input(' select project type: ')
                    options = xrange(1, pro_types_len + 1, 1)
                except NameError:
                    options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        type_selected = types[int(input_type) - 1]
                        pro_type_id = int(input_type) - 1
                        break
                    raise ValueError
                except ValueError:
                    error_message(
                        ProjectSelector.GEN_VERBOSE,
                        'not an appropriate choice'
                    )
            verbose_message(
                ProjectSelector.GEN_VERBOSE, verbose,
                'selected', type_selected
            )
        return type_selected, pro_type_id

    def __str__(self):
        '''
            Dunder method for ProjectSelector.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ()'.format(self.__class__.__name__)
