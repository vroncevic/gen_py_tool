# -*- coding: UTF-8 -*-

'''
 Module
     schema_container.py
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
     Defined class SchemaContainer with attribute(s) and method(s).
     Created API for schema container.
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


class SchemaContainer:
    '''
        Defined class SchemaContainer with attribute(s) and method(s).
        Created API for schema container.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __verbose - enable/disable verbose option.
                | __schema - schema object.
            :methods:
                | __init__ - initial constructor.
                | schema - get/set property schema object.
                | is_schema_ok - checking is project schema ok.
                | __str__ - dunder method for SchemaContainer.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::SCHEMA::SCHEMA_CONTAINER'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        self.__verbose = verbose
        self.__schema = None
        verbose_message(
            SchemaContainer.GEN_VERBOSE, verbose, 'init schema API util'
        )

    @property
    def schema(self):
        '''
            Get schema object property.

            :return: schema object | None.
            :rtype: <dict> | <NoneType>
            :exceptions: None
        '''
        return self.__schema

    @schema.setter
    def schema(self, schema):
        '''
            Set schema object property.

            :param schema: schema object.
            :type schema: <dict>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('dict:schema', schema)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__schema = schema
        verbose_message(
            SchemaContainer.GEN_VERBOSE, self.__verbose, 'set schema', schema
        )

    def is_schema_ok(self):
        '''
            Checking is project schema ok.

            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.__schema is not None, isinstance(self.__schema, dict)
        ])

    def __str__(self):
        '''
            Dunder method for SchemaContainer.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), str(self.__schema)
        )
