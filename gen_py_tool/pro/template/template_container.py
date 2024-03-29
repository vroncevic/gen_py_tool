# -*- coding: UTF-8 -*-

'''
 Module
     template_container.py
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
     Defined class TemplateContainer with attribute(s) and method(s).
     Created API for template container.
'''

import sys

try:
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


class TemplateContainer:
    '''
        Defined class TemplateContainer with attribute(s) and method(s).
        Created API for template container.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __verbose - enable/disable verbose option.
                | __template - template object.
            :methods:
                | __init__ - initial constructor.
                | template - get/set property template object.
                | is_template_ok - checking is project template ok.
                | __str__ - dunder method for TemplateContainer.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::TEMPLATE::TEMPLATE_CONTAINER'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        self.__verbose = verbose
        self.__template = None
        verbose_message(
            TemplateContainer.GEN_VERBOSE, verbose, 'init template API util'
        )

    @property
    def template(self):
        '''
            Get template object property.

            :return: template object | None.
            :rtype: <dict> | <NoneType>
            :exceptions: None
        '''
        return self.__template

    @template.setter
    def template(self, template):
        '''
            Set template object property.

            :param template: template object.
            :type template: <dict>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([('dict:template', template)])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.__template = template
        verbose_message(
            TemplateContainer.GEN_VERBOSE, self.__verbose,
            'set template', template
        )

    def is_template_ok(self):
        '''
            Checking is project template ok.

            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.__template is not None, isinstance(self.__template, dict)
        ])

    def __str__(self):
        '''
            Dunder method for TemplateContainer.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__verbose), str(self.__template)
        )
