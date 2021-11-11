# -*- coding: UTF-8 -*-

'''
 Module
     element_keys.py
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
     Defined class ElementKeys with attribute(s).
     Created attributes for processing tool/gen element.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ElementKeys:
    '''
        Defined class ElementKeys with attribute(s).
        Created attributes for processing tool/gen element.
        It defines:

            :attributes:
                | ROOT_KEY - element key for elements.
                | TOOL_NAME_KEY - element key for TOOL_NAME.
                | TOOL_UPPER_KEY - element key for TOOL_UPPER.
                | TOOL_CLASS_KEY - element key for TOOL_CLASS.
                | TOOL_YEAR_KEY - element key for YEAR.
            :methods:
                | None.
    '''

    ROOT_KEY = 'elements'
    TOOL_NAME_KEY = 'TOOL_NAME'
    TOOL_UPPER_KEY = 'TOOL_UPPER'
    TOOL_CLASS_KEY = 'TOOL_CLASS'
    TOOL_YEAR_KEY = 'YEAR'
