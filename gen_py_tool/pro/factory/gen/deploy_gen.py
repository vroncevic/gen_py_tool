# -*- coding: UTF-8 -*-

'''
 Module
     gen_extractor.py
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
     Defined class DeployGen with attribute(s) and method(s).
     Created API for extracting elements from schema for generator.
'''

import sys

try:
    from gen_py_tool.pro.element.element_keys import ElementKeys
    from gen_py_tool.pro.factory.extractiner.gen import ProExtractor
    from gen_py_tool.pro.factory.gen.gen_elements import GenElements
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
__status__ = 'extractd'


class DeployGen(ProExtractor, GenElements, ElementKeys):
    '''
        Defined class DeployGen with attribute(s) and method(s).
        Created API for extracting elements from schema for generator.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | deploy_gen - deployment of gen from project schema.
                | __str__ - dunder method for DeployGen.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::FACTORY::GEN::DEPLOY_GEN'

    def __init__(self, element, schema, verbose=False):
        '''
            Initial constructor.

            :param element: project elements.
            :type element: <dict>
            :param schema: schema for project tool.
            :type schema: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
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
        ProExtractor.__init__(self)
        self.element = element
        self.schema = schema
        verbose_message(DeployGen.GEN_VERBOSE, verbose, 'init extract gen')

    def deploy_modules(self):
        '''
            Deployment of gen from project schema.

            :return: list with gen name and modules.
            :rtype: <list>
            :exceptions: None
        '''
        gen_modules = []
        gen_name = self.extract_gen_name()
        gen_modules.append(gen_name)
        class_content, class_module = self.extract_gen_class()
        gen_modules.append([
            class_content, '{0}/{1}'.format(gen_name, class_module)
        ])
        edit_content, edit_module = self.extract_edit_config()
        gen_modules.append([
            edit_content, '{0}/{1}'.format(gen_name, edit_module)
        ])
        run_content, run_module = self.extract_gen_run()
        gen_modules.append([
            run_content, '{0}/run/{1}'.format(gen_name, run_module)
        ])
        gen_modules.append([
            edit_content, '{0}/run/{1}'.format(gen_name, edit_module)
        ])
        pro_content, pro_module = self.extract_gen_pro()
        gen_modules.append([
            pro_content, '{0}/pro/{1}'.format(gen_name, pro_module)
        ])
        read_content, read_module = self.extract_read_template()
        gen_modules.append([
            read_content, '{0}/pro/{1}'.format(gen_name, read_module)
        ])
        write_content, write_module = self.extract_write_template()
        gen_modules.append([
            write_content, '{0}/pro/{1}'.format(gen_name, write_module)
        ])
        gen_modules.append([
            edit_content, '{0}/pro/{1}'.format(gen_name, edit_module)
        ])
        conf_content, conf_module = self.extract_gen_conf()
        gen_modules.append([
            conf_content, '{0}/conf/{1}'.format(gen_name, conf_module)
        ])
        conf_util_content, conf_util_module = self.extract_gen_conf_util()
        gen_modules.append([
            conf_util_content, '{0}/conf/{1}'.format(
                gen_name, conf_util_module
            )
        ])
        template_content, template_module = self.extract_gen_conf_template()
        gen_modules.append([
            template_content, '{0}/conf/template/{1}'.format(
                gen_name, template_module
            )
        ])
        gen_modules.append([
            edit_content, '{0}/conf/{1}'.format(gen_name, edit_module)
        ])
        log_content, log_module = self.extract_gen_log()
        gen_modules.append([
            log_content, '{0}/log/{1}'.format(gen_name, log_module)
        ])
        gen_modules.append([
            edit_content, '{0}/log/{1}'.format(gen_name, edit_module)
        ])
        return gen_modules

    def __str__(self):
        '''
            Dunder method for DeployGen.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, ProExtractor.__str__(self)
        )
