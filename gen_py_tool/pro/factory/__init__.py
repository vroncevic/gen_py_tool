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
     Defined class Factory with attribute(s) and method(s).
     Created API for project container factory.
'''

import sys

try:
    from gen_py_tool.pro.factory.tool import ToolFactory
    from gen_py_tool.pro.factory.gen import GenFactory
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
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


class Factory:
    '''
        Defined class Factory with attribute(s) and method(s).
        Created API for project container factory.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __supported_pro_types - list with supported project types.
            :methods:
                | __init__ - initial constructor.
                | check_pro_type - checking project type is it supported.
                | produce - preparing project factory object.
                | __str__ - dunder method for Factory.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::FACTORY'

    def __init__(self, pro_types, verbose=False):
        '''
            Initial constructor.

            :param pro_types: project types.
            :type pro_types: <list>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('list:pro_types', pro_types)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__supported_pro_types = pro_types
        verbose_message(
            Factory.GEN_VERBOSE, verbose,
            'supported project types', pro_types
        )

    def check_pro_type(self, pro_type, verbose=False):
        '''
            Checking project type is it supported.

            :param pro_type: project type.
            :type pro_type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (supported) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('str:pro_type', pro_type)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status = False
        if pro_type in self.__supported_pro_types:
            status = True
        verbose_message(
            Factory.GEN_VERBOSE, verbose, 'project type',
            pro_type, 'supported', status
        )
        return status

    def produce(self, pro_property, schema, template, element, verbose=False):
        '''
            Preparing project factory object.

            :param pro_property: project property (name and type).
            :type pro_property: <dict>
            :param template: project tool/generator template.
            :type template: <dict>
            :param schema: project tool/generator schema.
            :type schema: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: factory product object | None.
            :rtype: <Python Object> | <NoneType>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:pro_property', pro_property),
            ('dict:schema', schema),
            ('dict:template', template),
            ('dict:element', element)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        product_container = None
        if self.check_pro_type(pro_property['type'], verbose=verbose):
            if self.__supported_pro_types[0] == pro_property['type']:
                product_container = ToolFactory(
                    pro_property, schema, template, element, verbose=verbose
                )
            if self.__supported_pro_types[1] == pro_property['type']:
                product_container = GenFactory(
                    pro_property, schema, template, element, verbose=verbose
                )
        else:
            error_message(
                Factory.GEN_VERBOSE, 'not supported project type',
                pro_property['type']
            )
        return product_container

    def __str__(self):
        '''
            Dunder method for Factory.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, self.__supported_pro_types
        )
