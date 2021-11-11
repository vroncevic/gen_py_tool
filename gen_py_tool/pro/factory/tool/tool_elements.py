# -*- coding: UTF-8 -*-

'''
 Module
     tool_elements.py
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
     Defined class ToolElements with attribute(s).
     Created attributes for preparing project schema for tool.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ToolElements:
    '''
        Defined class ToolElements with attribute(s).
        Created attributes for preparing project schema for tool.
        It defines:

            :attributes:
                | NAME - project type for tool.
                | MOD - project type for generator.
                | INIT - project type for tool.
                | RUN - project type for generator.
                | CLASS - project type for tool.
                | EDIT - project type for generator.
                | _EDIT - project type for tool.
                | CONF - project type for generator.
                | CFG - project type for tool.
                | CONFIG - project type for generator.
                | LOG - project type for tool.
                | UTIL - project type for generator.
            :methods:
                | None.
    '''

    NAME, MOD, INIT, RUN = 'tool_name', 'modules', '__init__.py', 'run'
    CLASS, EDIT, _EDIT = 'tool_name_class', 'editorconfig', '.editorconfig'
    CONF, CFG, CONFIG = 'conf', 'cfg', 'configuration'
    LOG, UTIL = 'log', 'util'
