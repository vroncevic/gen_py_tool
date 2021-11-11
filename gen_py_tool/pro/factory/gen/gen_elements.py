# -*- coding: UTF-8 -*-

'''
 Module
     gen_elements.py
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
     Defined class GenElements with attribute(s).
     Created attributes for preparing project schema for generator.
'''

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenElements:
    '''
        Defined class GenElements with attribute(s).
        Created attributes for preparing project schema for generator.
        It defines:

            :attributes:
                | NAME - project type for generator.
                | MOD - project type for generator.
                | INIT - project type for generator.
                | RUN - project type for generator.
                | CLASS - project type for generator.
                | EDIT - project type for generator.
                | _EDIT - project type for generator.
                | CONF - project type for generator.
                | CFG - project type for generator.
                | CONFIG - project type for generator.
                | LOG - project type for generator.
                | UTIL - project type for generator.
            :methods:
                | None.
    '''

    NAME, MOD, INIT, RUN = 'generator_name', 'modules', '__init__.py', 'run'
    CLASS, IO_CLASS = 'generator_process_class', 'io_class'
    EDIT, _EDIT = 'editorconfig', '.editorconfig'
    CONF, CFG, CONFIG, TEMPLATE = 'conf', 'cfg', 'configuration', 'template'
    PRO, LOG, UTIL, TEST = 'pro', 'log', 'util', 'generator_test'
    READ, WRITE = 'read_template', 'write_template'
