# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Define class GenTool with attribute(s) and method(s).
     Generate python tool by templates and parameters.
'''

import sys

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from gen_py_tool.pro.read_template import ReadTemplate
    from gen_py_tool.pro.write_template import WriteTemplate
    from gen_py_tool.pro.schema_selector import SchemaSelector
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.success import success_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenTool(FileChecking):
    '''
        Define class GenPro with attribute(s) and method(s).
        Generate project by templates and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots.
                | VERBOSE - Console text indicator for current process-phase.
                | __PRO_STRUCTURE - Project structure.
                | __config - Configuration dictionary.
                | __reader - Reader API.
                | __writer - Writer API.
            :methods:
                | __init__ - Initial constructor.
                | get_reader - Getter for reader object.
                | get_writer - Getter for writer object.
                | gen_project - Generate python tool.
    '''

    __slots__ = (
        'VERBOSE', '__PRO_STRUCTURE', '__config', '__reader', '__writer'
    )
    VERBOSE = 'GEN_PY_TOOL::PRO::GEN_TOOL'
    __PRO_STRUCTURE = '../conf/project.yaml'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: Parameter tool name.
            :type project_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params(
            [('str:project_name', project_name)]
        )
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        verbose_message(GenTool.VERBOSE, verbose, 'init generator')
        FileChecking.__init__(self, verbose=verbose)
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project = '{0}/{1}'.format(
            Path(__file__).parent, GenTool.__PRO_STRUCTURE
        )
        self.check_path(file_path=project, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project)
            self.__config = yml2obj.read_configuration()
        else:
            self.__config = None

    def get_reader(self):
        '''
            Getter for reader object.

            :return: Read template object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for writer object.

            :return: Write template object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_tool(self, verbose=False):
        '''
            Generate project structure.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Boolean status True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if bool(self.__config):
            tool_types, schema_files = [
                tool_type.keys()[0] for tool_type in self.__config['templates']
            ], self.__config['schema']
            schema_selector = SchemaSelector(tool_types, schema_files)
            schema, schema_id = schema_selector.get_schema()
            if schema and schema_id is not None:
                print(self.__config['templates'][schema_id])
                # read templates by read API
                # provide templates and schema to write API
            import pdb;pdb.set_trace()
        return True if status else False
