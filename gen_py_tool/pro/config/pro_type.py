# -*- coding: UTF-8 -*-

'''
 Module
     pro_type.py
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
     Defined class ProType with attribute(s) and method(s).
     Defined API for project type with preparations for generation.
'''

import sys

try:
    from ats_utilities.checker import ATSChecker
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


class ProType:
    '''
        Defined class ProType with attribute(s) and method(s).
        Defined API for project type with preparations for generation.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __verbose - enable/disable verbose option.
                | __pro_type - project type.
            :methods:
                | __init__ - initial constructor.
                | pro_type - property methods for set/get operations.
                | is_pro_type_ok - checking is project type ok.
                | __str__ - dunder method for ProType.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::CONFIG::PRO_TYPE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__pro_type = None
        verbose_message(ProType.GEN_VERBOSE, verbose, 'init project type')

    @property
    def pro_type(self):
        '''
            Property method for getting project type.

            :return: formatted project type | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.__pro_type

    @pro_type.setter
    def pro_type(self, pro_type):
        '''
            Property method for setting project type.

            :param pro_type: set project type.
            :type pro_type: <str>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:pro_type', pro_type)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__pro_type = pro_type
        verbose_message(
            ProType.GEN_VERBOSE, self.__verbose, 'set project type', pro_type
        )

    def is_pro_type_ok(self):
        '''
            Checking is project type ok.

            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.__pro_type is not None, isinstance(self.__pro_type, str)
        ])

    def __str__(self):
        '''
            Dunder method for ProType.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), self.__pro_type
        )
