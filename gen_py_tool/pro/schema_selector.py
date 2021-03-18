# -*- coding: UTF-8 -*-

'''
 Module
     schema_selector.py
 Copyright
     Copyright (C) 2019 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define class SchemaSelector with attribute(s) and method(s).
     Selecting tool for generating process of project structure.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SchemaSelector(FileChecking):
    '''
        Define class SchemaSelector with attribute(s) and method(s).
        Selecting tool for generating process of project structure.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __CONF - Configuration directory.
                | __schema - Schema object.
                | __schema_id - Schema ID.
            :methods:
                | __init__ - Initial constructor.
                | get_schema - Get schema objects.
                | __choose_schema - Select schema type.
    '''

    __slots__ = ('VERBOSE', '__CONF', '__schema', '__schema_id')
    VERBOSE = 'GEN_PY_TOOL::PRO::SCHEMA_SELECTOR'
    __CONF = '/../conf/'

    def __init__(self, tool_types, schema_files, verbose=False):
        '''
            Initial constructor.

            :param tool_types: List with tool types.
            :type tool_types: <list>
            :param schema_files: List with schema files.
            :type schema_files: <list>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('list:tool_types', tool_types),
            ('list:schema_files', schema_files)
        ])
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(SchemaSelector.VERBOSE, verbose, 'init tool selector')
        schema, schema_list = None, []
        FileChecking.__init__(self, verbose=verbose)
        for schema_file in schema_files:
            schema_list.append('{0}{1}{2}'.format(
                Path(__file__).parent, SchemaSelector.__CONF, schema_file
            ))
        schema = self.__choose_schema(tool_types, verbose=verbose)
        self.check_path(
            file_path=schema_list[int(schema) - 1], verbose=verbose
        )
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=schema_list[int(schema) - 1],
            file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(schema_list[int(schema) - 1])
            self.__schema = yml2obj.read_configuration()
        else:
            self.__schema = None
            self.__schema = None

    def get_schema(self):
        '''
            Get schema objects.

            :return: Schema objects | None None.
            :rtype: <dict> <int> | <NoneType> <NoneType>
            :exceptions: None
        '''
        return self.__schema, self.__schema_id

    def __choose_schema(self, tool_types, verbose=False):
        '''
            Select schema type.

            :param tool_types: List with tool types.
            :type tool_types: <list>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Tool type | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        tool_types_len = len(tool_types)
        for index, tool_type in enumerate(tool_types):
            print('{0} {1} schema'.format(index + 1, tool_type.capitalize()))
        while True:
            try:
                try:
                    input_type = raw_input(' select schema: ')
                except NameError:
                    input_type = input(' select schema: ')
                options = xrange(1, tool_types_len + 1, 1)
            except NameError:
                options = range(1, tool_types_len + 1, 1)
            try:
                if int(input_type) in list(options):
                    self.__schema_id = int(input_type) - 1
                    break
                else:
                    raise ValueError
            except ValueError:
                error_message(
                    SchemaSelector.VERBOSE, 'not an appropriate choice.'
                )
        verbose_message(
            SchemaSelector.VERBOSE, verbose, 'selected option', input_type
        )
        return input_type
