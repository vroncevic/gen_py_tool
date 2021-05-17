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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for writing a template content with parameters to a file.
'''

import sys
from os import chmod, getcwd
from string import Template

try:
    #from gen_py_tool.pro.element.element_keys import ElementKeys
    #from gen_py_tool.pro.schema import SchemaLoader
    #from gen_py_tool.pro.factory.tool.tool_extractor import ExtTool
    #from gen_py_tool.pro.factory.gen.gen_extractor import ExtGen
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for writing a template content with parameters to a file.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | write - write templates content with parameters to modules.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, element, schema, verbose=False):
        '''
            Write templates content with parameters to modules.

            :param element: processes element.
            :type element: <dict>
            :param schema: schema for tool/generator.
            :type schema: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:element', element), ('dict:schema', schema)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        modules, status, extractor = [], False, None
#        schema_root_key = schema.keys()[0]
#        if schema_root_key == SchemaLoader.TOOL_SCHEMA:
#            extractor = ExtTool(element, schema, verbose=verbose)
#            modules = extractor.deploy_tool()
#        elif schema_root_key == SchemaLoader.GEN_SCHEMA:
#            extractor = ExtGen(element, schema, verbose=verbose)
#            modules = extractor.deploy_gen()
#        if all([bool(extractor), bool(modules)]):
            #extractor.create_package_structure()
#            for template_content in modules[1:]:
#                template = Template(template_content[0])
#                module_content = template.substitute({
#                    ElementKeys.TOOL_NAME_KEY: '{0}'.format(
#                        element[ElementKeys.ROOT_KEY][0][
#                            ElementKeys.TOOL_NAME_KEY
#                        ]
#                    ),
#                    ElementKeys.TOOL_UPPER_KEY:'{0}'.format(
#                        element[ElementKeys.ROOT_KEY][1][
#                            ElementKeys.TOOL_UPPER_KEY
#                        ]
#                    ),
#                    ElementKeys.TOOL_CLASS_KEY:'{0}'.format(
#                        element[ElementKeys.ROOT_KEY][2][
#                            ElementKeys.TOOL_CLASS_KEY
#                        ]
#                    ),
#                    ElementKeys.TOOL_YEAR_KEY:'{0}'.format(
#                        element[ElementKeys.ROOT_KEY][3][
#                            ElementKeys.TOOL_YEAR_KEY
#                        ]
#                    )
#                })
#                import pdb;pdb.set_trace()
#                module_path = '{0}/{1}.py'.format(
#                    getcwd(), element['elements'][0]
#                )
#                with open(module_path, 'w') as module_file:
#                    module_file.write(module_content)
#                    chmod(module_path, 0o666)
#                status = False
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
