# -*- coding: UTF-8 -*-

'''
 Module
     base.py
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
     Defined class BaseExtractor with attribute(s) and method(s).
     Defined project container for post-processing phase.
'''

import sys

try:
    from gen_py_tool.pro.schema.schema_container import SchemaContainer
    from gen_py_tool.pro.element.element_container import ElementContainer
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


class BaseExtractor(SchemaContainer, ElementContainer):
    '''
        Defined class BaseExtractor with attribute(s) and method(s).
        Defined project container for post-processing phase.
        It defines:

            :attributes:
                | None.
            :methods:
                | __init__ - initial constructor.
                | is_container_ok - checking is container ok.
                | __str__ - dunder method for BaseExtractor.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        SchemaContainer.__init__(self, verbose=verbose)
        ElementContainer.__init__(self, verbose=verbose)

    def is_container_ok(self):
        '''
            Checking is container ok.

            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([self.is_schema_ok(), self.is_element_ok()])

    def __str__(self):
        '''
            Dunder method for BaseExtractor.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, str(self.__schema), str(self.__element)
        )
