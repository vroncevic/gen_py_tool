# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Define class WriteTemplate with attribute(s) and method(s).
     Write a template content with parameters to a file.
'''

import sys
from time import strftime
from os.path import exists
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.verbose import verbose_message
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


class WriteTemplate(object):
    '''
        Define class WriteTemplate with attribute(s) and method(s).
        Write a template content with parameters to a file.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __EDITOR_CONFIG - GitHub online editor configuration
                | __EDITOR_CONFIG_PY - Python extension name
                | __EDITOR_CONFIG_CFG - Configuration extension name
                | __CLASS - Class key for template
                | __FILE - File key for template
                | __DATE - Date key for template
            :methods:
                | __init__ - Initial constructor
                | write - Write templates content with parameters to modules.
    '''

    __slots__ = ('VERBOSE', '__ELEMENTS')
    VERBOSE = 'GEN_PY_TOOL::PRO::WRITE_TEMPLATE'
    __ELEMENTS = '/../conf/substitute_tool.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(WriteTemplate.VERBOSE, verbose, 'init writer')

    def gen_class_name(self, project_name, verbose=False):
        '''
            Generate class name.

            :param project_name: Project name.
            :type project_name: <str>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Class processed name for tool.
            :rtype: <str>
            :exceptions: None
        '''
        class_name =''
        split_project_name = project_name.split('_')
        if len(split_project_name) > 1:
            for index, part_name in enumerate(split_project_name):
                split_project_name[index] = part_name.capitalize()
        else:
            split_project_name[0] = project_name.capitalize()
        return class_name.join(split_project_name)

    def write(self, project_name, templates, schema, verbose=False):
        '''
            Write templates content with parameters to modules.

            :param project_name: Project name.
            :type project_name: <str>
            :param templates: List with templates.
            :type templates: <list>
            :param schema: Schema for tool/generator.
            :type schema: <dict>
            :param verbose: Enable/disable verbose option.
            :type verbose: <bool>
            :return: Boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:project_name', project_name),
            ('list:templates', templates),
            ('dict:schema', schema)
        ])
        if status == ATSChecker.TYPE_ERROR: raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR: raise ATSBadCallError(error)
        print()
        import pdb;pdb.set_trace()
        print(templates)
        print(schema)
        template, status = Template(content), False
        module_content = template.substitute({
            WriteTemplate.TOOL_NAME: '{0}'.format(project_name.lower()),
            WriteTemplate.TOOL_UPPER:'{0}'.format(project_name.upper()),
            WriteTemplate.TOOL_CLASS:'{0}'.format(
                self.gen_class_name(project_name, verbose=verbose)
            ),
            WriteTemplate.YEAR:'{0}'.format(strftime("%Y"))
        })
        module_path = '{0}/{1}'.format(self.__pro_dir, module_name)
        with open(module_path, 'w') as module_file:
            
            module_file.write(module_content)
            chmod(module_path, 0o666)
        status = False
        return True if status else False
