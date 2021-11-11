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
     from gen_py_tool.pro.factory.collectiner.gen.base import BaseCollectiner
     from gen_py_tool.pro.factory.gen.gen_elements import GenElements
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
                | update_gen_name - peparing gen name for project.
                | update_gen_class - preparing gen class for project.
                | update_gen_run - preparing gen run for project.
                | update_gen_pro_class - preparing gen class for project.
                | update_gen_conf - preparing gen conf for project.
                | update_gen_log - preparing gen log for project.
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

    def update_gen_name(self):
        '''
            Preparing generator name for project schema.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name] = self.schema[
            schema_root_key
        ].pop(GenElements.NAME)

    def update_gen_class(self):
        '''
            Preparing generator project setup.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][0][
            GenElements.INIT
        ] = self.template[self.pro_type][0][GenElements.CLASS]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][1][
            GenElements._EDIT
        ] = self.template[self.pro_type][1][GenElements.EDIT]

    def update_gen_run(self):
        '''
            Preparing generator project setup.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][2][
            GenElements.RUN
        ][GenElements.MOD][0][
            '{0}_{1}.py'.format(self.pro_name, GenElements.RUN)
        ] = self.schema[schema_root_key][self.pro_name][GenElements.MOD][2][
            GenElements.RUN
        ][GenElements.MOD][0].pop('{0}_{1}.py'.format(
            GenElements.NAME, GenElements.RUN
        ))
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][2][
            GenElements.RUN
        ][GenElements.MOD][0]['{0}_{1}.py'.format(
            self.pro_name, GenElements.RUN
        )] = self.template[self.pro_type][2][
            '{0}_{1}'.format(GenElements.RUN, self.pro_type)
        ]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][2][
            GenElements.RUN
        ][GenElements.MOD][1][
            GenElements._EDIT
        ] = self.template[self.pro_type][1][GenElements.EDIT]

    def update_gen_pro_class(self):
        '''
            Preparing generator project class setup.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][0][GenElements.INIT] = self.template[
            self.pro_type
        ][3]['{0}_{1}'.format(self.pro_type, GenElements.IO_CLASS)]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][1]['{0}.py'.format(
            GenElements.READ
        )] = self.template[self.pro_type][4]['{0}_{1}'.format(
            self.pro_type, GenElements.READ
        )]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][2]['{0}.py'.format(
            GenElements.WRITE
        )] = self.template[self.pro_type][5]['{0}_{1}'.format(
            self.pro_type, GenElements.WRITE
        )]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][3][
            GenElements.PRO
        ][GenElements.MOD][3][
            GenElements._EDIT
        ] = self.template[self.pro_type][1][GenElements.EDIT]

    def update_gen_conf(self):
        '''
            Preparing generator project setup.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][0]['{0}.{1}'.format(
            self.pro_name, GenElements.CFG
        )] = self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][0].pop('{0}.{1}'.format(
            GenElements.NAME, GenElements.CFG
        ))
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][0]['{0}.{1}'.format(
            self.pro_name, GenElements.CFG
        )] = self.template[self.pro_type][6]['{0}_{1}'.format(
            self.pro_type, GenElements.CONFIG
        )]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][1]['{0}_{1}.{2}'.format(
            self.pro_name, GenElements.UTIL, GenElements.CFG
        )] = self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][1].pop('{0}_{1}.{2}'.format(
            GenElements.NAME, GenElements.UTIL, GenElements.CFG
        ))
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][1]['{0}_{1}.{2}'.format(
            self.pro_name, GenElements.UTIL, GenElements.CFG
        )] = self.template[self.pro_type][7]['{0}_{1}_{2}'.format(
            self.pro_type, GenElements.CONFIG, GenElements.UTIL
        )]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][2][GenElements._EDIT] = self.template[
            self.pro_type][1][GenElements.EDIT]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][3][GenElements.TEMPLATE][GenElements.MOD][0][
            '{0}.{1}'.format(GenElements.TEST, GenElements.TEMPLATE)
        ] = self.template[self.pro_type][8]['{0}'.format(GenElements.TEST)]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][4][
            GenElements.CONF
        ][GenElements.MOD][3][GenElements.TEMPLATE][GenElements.MOD][1][
            GenElements._EDIT
        ] = self.template[self.pro_type][1][GenElements.EDIT]

    def update_gen_log(self):
        '''
            Preparing generator project setup.

            :exceptions: None
        '''
        schema_root_key = self.schema.keys()[0]
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][0]['{0}.{1}'.format(
            self.pro_name, GenElements.LOG
        )] = self.schema[schema_root_key][self.pro_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][0].pop('{0}.{1}'.format(
            GenElements.NAME, GenElements.LOG
        ))
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][0]['{0}.{1}'.format(
            self.pro_name, GenElements.LOG
        )] = ''
        self.schema[schema_root_key][self.pro_name][GenElements.MOD][5][
            GenElements.LOG
        ][GenElements.MOD][1][
            GenElements._EDIT
        ] = self.template[self.pro_type][1][GenElements.EDIT]

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
