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
     Defined class ProExtractor with attribute(s) and method(s).
     Defined project container for post-processing phase.
'''

import sys
from os import getcwd, mkdir

try:
    from gen_py_tool.pro.element.element_keys import ElementKeys
    from gen_py_tool.pro.factory.tool.tool_elements import ToolElements
    from gen_py_tool.pro.factory.extractiner.tool.base import BaseExtractor
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


class ProExtractor(BaseExtractor):
    '''
        Defined class ProExtractor with attribute(s) and method(s).
        Defined project container for post-processing phase.
        It defines:

            :attributes:
                | None.
            :methods:
                | __init__ - initial constructor.
                | extract_tool_name - extract tool name for project.
                | extract_tool_class - extract tool class for project.
                | extract_tool_run - extract tool run for project.
                | extract_tool_conf - extract tool conf for project.
                | extract_tool_conf_util - extract tool conf util for project.
                | extract_tool_log - extract tool log for project.
                | extract_edit_config - extract tool edit config for project.
                | create_package_structure - create package structure.
                | __str__ - dunder method for ProExtractor.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        BaseExtractor.__init__(self, verbose=verbose)

    def extract_tool_name(self):
        '''
            Extraction of tool name from project element.

            :return: tool name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.element[ElementKeys.ROOT_KEY][0][ElementKeys.TOOL_NAME_KEY]

    def extract_tool_class(self):
        '''
            Extraction tool class from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = ToolElements.INIT
        return self.schema[schema_root_key][
            tool_name
        ][ToolElements.MOD][0][module_name], module_name

    def extract_tool_run(self):
        '''
            Extraction tool run from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = '{0}_{1}.py'.format(tool_name, ToolElements.RUN)
        return self.schema[schema_root_key][tool_name][ToolElements.MOD][2][
            ToolElements.RUN
        ][ToolElements.MOD][0][module_name], module_name

    def extract_tool_conf(self):
        '''
            Extraction tool conf from project schema.

            :return: ini configuraiton code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = '{0}.{1}'.format(tool_name, ToolElements.CFG)
        return self.schema[schema_root_key][tool_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][0][module_name], module_name

    def extract_tool_conf_util(self):
        '''
            Extraction tool conf util from project schema.

            :return: ini configuraiton code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = '{0}_{1}.{2}'.format(
            tool_name, ToolElements.UTIL, ToolElements.CFG
        )
        return self.schema[schema_root_key][tool_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][1][module_name], module_name

    def extract_tool_log(self):
        '''
            Extraction tool log from project schema.

            :return: empty log content | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = '{0}.{1}'.format(tool_name, ToolElements.LOG)
        return self.schema[schema_root_key][tool_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][0][module_name], module_name

    def extract_edit_config(self):
        '''
            Extraction tool edit config from project schema.

            :return: github edit configuration | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        tool_name = self.extract_tool_name()
        module_name = ToolElements._EDIT
        return self.schema[schema_root_key][tool_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][1][ToolElements._EDIT], module_name

    def create_package_structure(self):
        '''
            Creating tool package structure from project schema.

            :exceptions: None
        '''
        tool_name = self.extract_tool_name()
        package = '{0}/{1}'.format(getcwd(), tool_name)
        mkdir(package)
        run = '{0}/{1}'.format(package, 'run')
        mkdir(run)
        conf = '{0}/{1}'.format(package, 'conf')
        mkdir(conf)
        log = '{0}/{1}'.format(package, 'log')
        mkdir(log)

    def __str__(self):
        '''
            Dunder method for ProExtractor.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, BaseExtractor.__str__(self)
        )
