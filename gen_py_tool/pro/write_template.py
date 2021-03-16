# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
from datetime import date
from os.path import exists
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
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
                | write - Write a template content with parameters to a file
    '''

    __slots__ = (
        'VERBOSE',
    )
    VERBOSE = 'GEN_PY_TOOL::TOOL::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')

    def write(self, verbose=False):
        '''
            Write a template content with parameters to a file.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status, True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        '''
        status = False
        return True if status else False
