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
     Defined class SchemaLoader with attribute(s) and method(s).
     Created API for schema checking and loading.
'''

import sys

try:
    from pathlib import Path
    from gen_py_tool.pro.schema.schema_container import SchemaContainer
    from gen_py_tool.pro.schema.schema_keys import SchemaKeys
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
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


class SchemaLoader(FileChecking, SchemaContainer, SchemaKeys):
    '''
        Defined class SchemaLoader with attribute(s) and method(s).
        Created API for schema checking and loading.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONF_DIR - configuration directory.
            :methods:
                | __init__ - initial constructor.
                | check_root_key - check root key for schema.
                | __str__ - dunder method for SchemaLoader.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::SCHEMA::SCHEMA_LOADER'
    CONF_DIR = '/../../conf/schema/'

    def __init__(self, schema_file, verbose=False):
        '''
            Initial constructor.

            :param schema_file: schema file.
            :type schema_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:schema_file', schema_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        SchemaContainer.__init__(self, verbose=verbose)
        verbose_message(
            SchemaLoader.GEN_VERBOSE, verbose, 'init schema loader'
        )
        schema_path = '{0}{1}{2}'.format(
            Path(__file__).parent, SchemaLoader.CONF_DIR, schema_file
        )
        self.check_path(file_path=schema_path, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=schema_path, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(schema_path)
            self.schema = yml2obj.read_configuration(verbose=verbose)

    def check_root_key(self, verbose=False):
        '''
            Check root key for schema.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if bool(self.schema):
            for root_key in self.schema.keys():
                if root_key in SchemaLoader.SUPPORTED_SCHEMAS:
                    status = True
        verbose_message(
            SchemaLoader.GEN_VERBOSE, verbose, 'defined key', status
        )
        return status

    def __str__(self):
        '''
            Dunder method for SchemaLoader.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            SchemaContainer.__str__(self)
        )
