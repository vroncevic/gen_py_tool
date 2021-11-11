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
     Defined class TemplateLoader with attribute(s) and method(s).
     Created API for template checking and loadig.
'''

import sys

try:
    from pathlib import Path
    from gen_py_tool.pro.template.template_container import TemplateContainer
    from gen_py_tool.pro.template.template_keys import TemplateKeys
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
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


class TemplateLoader(FileChecking, TemplateContainer, TemplateKeys):
    '''
        Defined class TemplateLoader with attribute(s) and method(s).
        Created API for template checking and loadig.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONF_DIR - configuration directory.
            :methods:
                | __init__ - initial constructor.
                | check_root_key - check root key for template.
                | __str__ - dunder method for TemplateLoader.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::TEMPLATE::TEMPLATE_LOADER'
    CONF_DIR = '/../../conf/template/'

    def __init__(self, template_file, verbose=False):
        '''
            Initial constructor.

            :param template_file: template file.
            :type template_file: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:template_file', template_file)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        FileChecking.__init__(self, verbose=verbose)
        TemplateContainer.__init__(self, verbose=verbose)
        verbose_message(
            TemplateLoader.GEN_VERBOSE, verbose, 'init template loader'
        )
        template_path = '{0}{1}{2}'.format(
            Path(__file__).parent, TemplateLoader.CONF_DIR, template_file
        )
        self.check_path(file_path=template_path, verbose=verbose)
        self.check_mode(file_mode='r', verbose=verbose)
        self.check_format(
            file_path=template_path,
            file_format='yaml', verbose=verbose
        )
        if self.is_file_ok():
            yml2obj = Yaml2Object(template_path)
            self.template = yml2obj.read_configuration(verbose=verbose)

    def check_root_key(self, verbose=False):
        '''
            Check root key for template.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if bool(self.template):
            for root_key in self.template.keys():
                if root_key in TemplateLoader.SUPPORTED_TEMPLATES:
                    status = True
        verbose_message(
            TemplateLoader.GEN_VERBOSE, verbose, 'defined key', status
        )
        return status

    def __str__(self):
        '''
            Dunder method for TemplateLoader.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            TemplateContainer.__str__(self)
        )
