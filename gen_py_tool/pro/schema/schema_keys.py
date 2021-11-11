# -*- coding: UTF-8 -*-

'''
 Module
     schema_keys.py
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
     Defined class SchemaKeys with attribute(s).
     Created attributes for processing tool/gen schema.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SchemaKeys:
    '''
        Defined class SchemaKeys with attribute(s).
        Created attributes for processing tool/gen schema.
        It defines:

            :attributes:
                | TOOL_SCHEMA - schema tool key.
                | GEN_SCHEMA - schema generator key.
                | SUPPORTED_SCHEMAS - supportd schemas (checks by key).
            :methods:
                | None.
    '''

    TOOL_SCHEMA, GEN_SCHEMA = 'schema_tool', 'schema_generator'
    SUPPORTED_SCHEMAS = [TOOL_SCHEMA, GEN_SCHEMA]
