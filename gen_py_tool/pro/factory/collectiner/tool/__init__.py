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
     Defined class ProCollectiner with attribute(s) and method(s).
     Defined project container for pre-processing phase.
'''

import sys

try:
     from gen_py_tool.pro.factory.collectiner.tool.base import BaseCollectiner
     from gen_py_tool.pro.factory.tool.tool_elements import ToolElements
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


class ProCollectiner(BaseCollectiner):
    '''
        Defined class ProCollectiner with attribute(s) and method(s).
        Defined project container for pre-processing phase.
        It defines:

            :attributes:
                | None.
            :methods:
                | __init__ - initial constructor.
                | update_tool_name - peparing tool name for project.
                | update_tool_class - preparing tool class for project.
                | update_tool_run - preparing tool run for project.
                | update_tool_conf - preparing tool conf for project.
                | update_tool_log - preparing tool log for project.
                | __str__ - dunder method for ProCollectiner.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        BaseCollectiner.__init__(self, verbose=verbose)

    def update_tool_name(self):
        '''
            Preparing tool name for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name] = self.schema[
            schema_root_key
        ].pop(ToolElements.NAME)

    def update_tool_class(self):
        '''
            Preparing tool class for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][0][
            ToolElements.INIT
        ] = self.template[self.pro_type][0][ToolElements.CLASS]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][1][
            ToolElements._EDIT
        ] = self.template[self.pro_type][1][ToolElements.EDIT]

    def update_tool_run(self):
        '''
            Preparing tool run for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][2][
            ToolElements.RUN
        ][ToolElements.MOD][0][
            '{0}_{1}.py'.format(self.pro_name, ToolElements.RUN)
        ] = self.schema[
            schema_root_key
        ][self.pro_name][ToolElements.MOD][2][
            ToolElements.RUN
        ][ToolElements.MOD][0].pop(
            '{0}_{1}.py'.format(ToolElements.NAME, ToolElements.RUN)
        )
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][2][
            ToolElements.RUN
        ][ToolElements.MOD][0][
            '{0}_{1}.py'.format(self.pro_name, ToolElements.RUN)
        ] = self.template[self.pro_type][2][
            '{0}_{1}'.format(ToolElements.RUN, self.pro_type)
        ]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][2][
            ToolElements.RUN
        ][ToolElements.MOD][1][
            ToolElements._EDIT
        ] = self.template[self.pro_type][1][ToolElements.EDIT]

    def update_tool_conf(self):
        '''
            Preparing tool conf for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][0][
            '{0}.{1}'.format(self.pro_name, ToolElements.CFG)
        ] = self.schema[
            schema_root_key
        ][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][0].pop(
            '{0}.{1}'.format(ToolElements.NAME, ToolElements.CFG)
        )
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][0][
            '{0}.{1}'.format(self.pro_name, ToolElements.CFG)
        ] = self.template[self.pro_type][3][
            '{0}_{1}'.format(self.pro_type, ToolElements.CONFIG)
        ]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][1][
            '{0}_{1}.{2}'.format(
                self.pro_name, ToolElements.UTIL, ToolElements.CFG
            )
        ] = self.schema[
            schema_root_key
        ][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][1].pop(
            '{0}_{1}.{2}'.format(
                ToolElements.NAME, ToolElements.UTIL, ToolElements.CFG
            )
        )
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][1][
            '{0}_{1}.{2}'.format(
                self.pro_name, ToolElements.UTIL, ToolElements.CFG
            )
        ] = self.template[self.pro_type][4][
            '{0}_{1}_{2}'.format(
                self.pro_type, ToolElements.CONFIG, ToolElements.UTIL
            )
        ]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][3][
            ToolElements.CONF
        ][ToolElements.MOD][2][
            ToolElements._EDIT
        ] = self.template[self.pro_type][1][ToolElements.EDIT]

    def update_tool_log(self):
        '''
            Preparing tool log for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][0][
            '{0}.{1}'.format(self.pro_name, ToolElements.LOG)
        ] = self.schema[
            schema_root_key
        ][self.pro_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][0].pop(
            '{0}.{1}'.format(ToolElements.NAME, ToolElements.LOG)
        )
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][0][
            '{0}.{1}'.format(self.pro_name, ToolElements.LOG)
        ] = ''
        self.schema[schema_root_key][self.pro_name][ToolElements.MOD][4][
            ToolElements.LOG
        ][ToolElements.MOD][1][
            ToolElements._EDIT
        ] = self.template[self.pro_type][1][ToolElements.EDIT]

    def __str__(self):
        '''
            Dunder method for ProCollectiner.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, BaseCollectiner.__str__(self)
        )
