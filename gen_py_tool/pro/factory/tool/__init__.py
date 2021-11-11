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
     Defined class ToolFactory with attribute(s) and method(s).
     Created API for preparing project schema for tool.
'''

import sys

try:
    from gen_py_tool.pro.factory.tool.prepare_tool import PrepareTool
    from gen_py_tool.pro.factory.tool.deploy_tool import DeployTool
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
__status__ = 'Updated'


class ToolFactory:
    '''
        Defined class ToolFactory with attribute(s) and method(s).
        Created API for preparing project schema for tool.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | get_preparer - get preparer object for factory.
                | get_deployer - get deployer object for factory.
                | __str__ - dunder method for ToolFactory.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::FACTORY::TOOL::TOOL_FACTORY'

    def __init__(self, pro_property, schema, template, element, verbose=False):
        '''
            Initial constructor.

            :param pro_property: project property.
            :type pro_property: <dict>
            :param schema: project tool/generator schema.
            :type schema: <dict>
            :param template: project tool/generator template.
            :type template: <dict>
            :param element: project tool/generator element.
            :type element: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:pro_property', pro_property),
            ('dict:schema', schema),
            ('dict:template', template),
            ('dict:element', element),
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.prepare_tool = PrepareTool(
            pro_property, template, schema, verbose=verbose
        )
        self.deploy_tool = DeployTool(element, schema, verbose=verbose)
        verbose_message(ToolFactory.GEN_VERBOSE, verbose, 'init prepare tool')

    def get_preparer(self):
        '''
            Get preparer object from ToolFactory for Factory.

            :return: object for preparing tool.
            :rtype: <PrepareTool>
            :exceptions: None
        '''
        return self.prepare_tool

    def get_deployer(self):
        '''
            Get deployer object from ToolFactory for Factory.

            :return: object for deploying tool.
            :rtype: <DeployTool>
            :exceptions: None
        '''
        return self.deploy_tool

    def __str__(self):
        '''
            Dunder method for ToolFactory.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.prepare_tool),
            str(self.deploy_tool)
        )
