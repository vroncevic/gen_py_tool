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
    from gen_py_tool.pro.factory.gen.gen_elements import GenElements
    from gen_py_tool.pro.factory.extractiner.gen.base import BaseExtractor
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
                | extract_gen_name - extract gen name for project.
                | extract_gen_class - extract gen class for project.
                | extract_gen_run - extract gen run for project.
                | extract_gen_conf - extract gen conf for project.
                | extract_gen_conf_util - extract gen conf util for project.
                | extract_gen_conf_template - extract gen template for project.
                | extract_gen_log - extract gen log for project.
                | extract_edit_config - extract gen edit config for project.
                | create_package_structure - create package structure.
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

    def extract_gen_name(self):
        '''
            Extraction of gen name from project element.

            :return: gen name | None.
            :rtype: <str> | <NoneType>
            :exceptions: None
        '''
        return self.element[ElementKeys.ROOT_KEY][0][ElementKeys.TOOL_NAME_KEY]

    def extract_gen_class(self):
        '''
            Extraction gen class from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = GenElements.INIT
        return self.schema[schema_root_key][
            gen_name
        ][GenElements.MOD][0][module_name], module_name

    def extract_gen_run(self):
        '''
            Extraction gen run from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}_{1}.py'.format(gen_name, GenElements.RUN)
        return self.schema[schema_root_key][gen_name][GenElements.MOD][2][
            GenElements.RUN
        ][GenElements.MOD][0][module_name], module_name

    def extract_gen_pro(self):
        '''
            Extraction gen pro from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = GenElements.INIT
        return self.schema[schema_root_key][gen_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][0][module_name], module_name

    def extract_read_template(self):
        '''
            Extraction gen pro from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}.py'.format(GenElements.READ)
        return self.schema[schema_root_key][gen_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][1][module_name], module_name

    def extract_write_template(self):
        '''
            Extraction gen pro from project schema.

            :return: python code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}.py'.format(GenElements.WRITE)
        return self.schema[schema_root_key][gen_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][2][module_name], module_name

    def extract_gen_conf(self):
        '''
            Extraction gen conf from project schema.

            :return: ini configuraiton code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}.{1}'.format(gen_name, GenElements.CFG)
        return self.schema[schema_root_key][gen_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][0][module_name], module_name

    def extract_gen_conf_util(self):
        '''
            Extraction gen conf util from project schema.

            :return: ini configuraiton code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}_{1}.{2}'.format(
            gen_name, GenElements.UTIL, GenElements.CFG
        )
        return self.schema[schema_root_key][gen_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][1][module_name], module_name

    def extract_gen_conf_template(self):
        '''
            Extraction gen conf template from project schema.

            :return: ini configuraiton code | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}.{1}'.format(
            GenElements.TEST, GenElements.TEMPLATE
        )
        return self.schema[schema_root_key][gen_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][3][GenElements.TEMPLATE][GenElements.MOD][0][
            module_name
        ], module_name

    def extract_gen_log(self):
        '''
            Extraction gen log from project schema.

            :return: empty log content | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = '{0}.{1}'.format(gen_name, GenElements.LOG)
        return self.schema[schema_root_key][gen_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][0][module_name], module_name

    def extract_edit_config(self):
        '''
            Extraction gen edit config from project schema.

            :return: github edit configuration | None.
            :rtype: <str>, <str> | <NoneType>, <str>
            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        gen_name = self.extract_gen_name()
        module_name = GenElements._EDIT
        return self.schema[schema_root_key][gen_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][1][GenElements._EDIT], module_name

    def create_package_structure(self):
        '''
            Creating generator package structure from project schema.

            :exceptions: None
        '''
        gen_name = self.extract_gen_name()
        package = '{0}/{1}'.format(getcwd(), gen_name)
        mkdir(package)
        pro = '{0}/{1}'.format(package, 'pro')
        mkdir(pro)
        run = '{0}/{1}'.format(package, 'run')
        mkdir(run)
        conf = '{0}/{1}'.format(package, 'conf')
        mkdir(conf)
        template = '{0}/{1}'.format(conf, 'template')
        mkdir(template)
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
