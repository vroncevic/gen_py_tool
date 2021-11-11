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
     Defined class GenPro with attribute(s) and method(s).
     Generate project by setup of parameters, templates, schemas.
'''

import sys

try:
    from pathlib import Path
    from gen_py_tool.pro.config import ProConfig
    from gen_py_tool.pro.config.pro_name import ProName
    from gen_py_tool.pro.config.pro_type import ProType
    from gen_py_tool.pro.config.pro_selector import ProjectSelector
    from gen_py_tool.pro.read_template import ReadTemplate
    from gen_py_tool.pro.write_template import WriteTemplate
    from gen_py_tool.pro.schema import SchemaLoader
    from gen_py_tool.pro.element import ElementLoader
    from gen_py_tool.pro.template import TemplateLoader
    from gen_py_tool.pro.factory import Factory
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
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


class GenPro(FileChecking, ProConfig, ProName, ProType):
    '''
        Defined class GenPro with attribute(s) and method(s).
        Generate project by setup of parameters, templates, schemas.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - project structure.
            :methods:
                | __init__ - initial constructor.
                | is_pro_config_ok - checking is project configuration ok.
                | gen_pro - generate project structure.
                | __str__ - dunder method for GenPro.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::GEN_PRO'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, project_name, verbose=False):
        '''
            Initial constructor.

            :param project_name: project tool/generator name.
            :type project_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:project_name', project_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        verbose_message(GenPro.GEN_VERBOSE, verbose, 'init generator')
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        ProType.__init__(self, verbose=verbose)
        project_structure = '{0}{1}'.format(
            Path(__file__).parent, GenPro.PRO_STRUCTURE
        )
        self.check_path(file_path=project_structure, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=project_structure, file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.config = yml2obj.read_configuration()
            self.pro_name = project_name

    def is_pro_config_ok(self, verbose=False):
        '''
            Checking is project configuration ok.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.is_config_ok(), ProjectSelector.check_config_keys(
                self.config, verbose=verbose
            )
        ])

    def gen_pro(self, verbose=False):
        '''
            Generate project structure.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.is_pro_config_ok(verbose=verbose):
            pro_type, pro_type_id = ProjectSelector.select_pro_type(
                self.config, verbose=verbose
            )
            self.pro_type = pro_type
            schema_loader = SchemaLoader(
                self.config[ProjectSelector.SCHEMA_KEY][pro_type_id],
                verbose=verbose
            )
            element_loader = ElementLoader(
                self.config[ProjectSelector.ELEMENT_KEY][pro_type_id],
                verbose=verbose
            )
            template_loader = TemplateLoader(
                self.config[ProjectSelector.TEMPLATE_KEY][pro_type_id],
                verbose=verbose
            )
            if self.is_pro_name_ok():
                status = element_loader.process_element(
                    self.pro_name, verbose=verbose
                )
            else:
                error_message(GenPro.GEN_VERBOSE, 'project name not ok')
            if status:
                status = all([
                    bool(schema_loader), bool(element_loader),
                    bool(template_loader)
                ])
                if status:
                    reader = ReadTemplate(verbose=verbose)
                    writer = WriteTemplate(verbose=verbose)
                    template, status = reader.read(
                        template_loader.template, self.pro_type,
                        verbose=verbose
                    )
                    if all([bool(template), bool(status)]):
                        project_property = {
                            'name': self.pro_name, 'type': self.pro_type
                        }
                        factory = Factory(
                            self.config['types'], verbose=verbose
                        )
                        product_container = factory.produce(
                            project_property, schema_loader.schema, template,
                            element_loader.element, verbose=verbose
                        )
                        preparer = product_container.get_preparer()
                        schema, status = preparer.export(verbose=verbose)
                        if all([bool(schema), bool(status)]):
                            deployer = product_container.get_deployer()
                            modules = deployer.deploy_modules()
                            deployer.create_package_structure()
                            status = writer.write(
                                element_loader.element, modules,
                                verbose=verbose
                            )
                        else:
                            error_message(
                                GenPro.GEN_VERBOSE,
                                'failed to prepare project schema'
                            )
                    else:
                        error_message(
                            GenPro.GEN_VERBOSE, 'failed to load templates'
                        )
                else:
                    error_message(
                        GenPro.GEN_VERBOSE, 'configuration keys not ok'
                    )
        else:
            error_message(
                GenPro.GEN_VERBOSE, 'configuration keys not ok'
            )
        return status

    def __str__(self):
        '''
            Dunder method for GenPro.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            ProType.__str__(self)
        )
