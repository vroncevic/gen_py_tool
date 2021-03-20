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
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
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
                | __project_name - Project name.
            :methods:
                | __init__ - Initial constructor.
                | get_reader - Getter for reader object.
                | get_writer - Getter for writer object.
                | get_tool_types - Get tool types.
                | get_schema_files -  Get schema files.
                | get_templates - Get template files.
                | gen_tool - Generate python tool.
    '''

    __slots__ = (
        'VERBOSE', '__PRO_STRUCTURE', '__config',
        '__reader', '__writer', '__project_name'
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
        self.__project_name = project_name
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

    def get_tool_types(self, verbose=False):
        '''
            Get tool types.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: List of tool types | empty list.
            :rtype: <list>
            :exceptions: None
        '''
        tool_types = []
        if bool(self.__config):
            for tool_type in self.__config['templates']:
                if len(tool_type.keys()) == 1:
                    verbose_message(
                        GenTool.VERBOSE, verbose, 'tool type: {0}'.format(
                            tool_type.keys()[0]
                        )
                    )
                    tool_types.append(tool_type.keys()[0])
                else:
                    error_message(
                        GenTool.VERBOSE, 'tool types: num of keys {0}'.format(
                            len(tool_type.keys())
                        )
                    )
                    break
        else:
            error_message(
                GenTool.VERBOSE, 'tool types: check configuration'
            )
        return tool_types

    def get_schema_files(self, verbose=False):
        '''
            Get schema files.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: List of schema files | empty list.
            :rtype: <list>
            :exceptions: None
        '''
        schema_files = []
        if bool(self.__config):
            verbose_message(GenTool.VERBOSE, verbose, 'schema files: setup')
            schema_files = self.__config['schema']
        else:
            error_message(
                GenTool.VERBOSE, 'schema files: check configuration'
            )
        return schema_files

    def get_templates(self, schema_id, verbose=False):
        '''
            Get template files.

            :param schema_id: Schema ID.
            :type schema_id: <int>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: List of template files | empty list.
            :rtype: <list>
            :exceptions: None
        '''
        templates = []
        if bool(self.__config):
            verbose_message(
                GenTool.VERBOSE, verbose,
                'template files: schema ID{0}'.format(schema_id)
            )
            templates = self.__config['templates'][schema_id]
        else:
            error_message(
                GenTool.VERBOSE, 'template files: check configuration'
            )
        return templates

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
        tool_types = self.get_tool_types(verbose=verbose)
        schema_files = self.get_schema_files(verbose=verbose)
        if all([bool(tool_types), bool(schema_files)]):
            schema_selector = SchemaSelector(
                tool_types, schema_files, verbose=verbose
            )
            schema, schema_id = schema_selector.get_schema()
            if schema and schema_id is not None:
                template_dict = self.get_templates(schema_id, verbose=verbose)
                if bool(template_dict):
                    templates, status = self.__reader.read(
                        template_dict, tool_types[schema_id], verbose=verbose
                    )
                    if all([status, bool(templates)]):
                        status = self.__writer.write(
                            self.__project_name, templates,
                            schema, verbose=verbose
                        )
        return True if status else False
