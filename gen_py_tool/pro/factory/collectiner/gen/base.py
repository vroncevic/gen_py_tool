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
     Defined class BaseCollectiner with attribute(s) and method(s).
     Defined project container for pre-processing phase.
'''

import sys

try:
    from gen_py_tool.pro.config.pro_name import ProName
    from gen_py_tool.pro.config.pro_type import ProType
    from gen_py_tool.pro.schema.schema_container import SchemaContainer
    from gen_py_tool.pro.template.template_container import TemplateContainer
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


class BaseCollectiner(ProName, ProType, SchemaContainer, TemplateContainer):
    '''
        Defined class BaseCollectiner with attribute(s) and method(s).
        Defined project container for pre-processing phase.
        It defines:

            :attributes:
                | None.
            :methods:
                | __init__ - initial constructor.
                | is_container_ok - checking is container ok.
                | __str__ - dunder method for BaseCollectiner.
    '''

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        ProName.__init__(self, verbose=verbose)
        ProType.__init__(self, verbose=verbose)
        SchemaContainer.__init__(self, verbose=verbose)
        TemplateContainer.__init__(self, verbose=verbose)

    def is_container_ok(self):
        '''
            Checking is container ok.

            :return: boolean status, True (ok) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        return all([
            self.is_pro_name_ok(), self.is_pro_type_ok(),
            self.is_schema_ok(), self.is_template_ok()
        ])

    def __str__(self):
        '''
            Dunder method for BaseCollectiner.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4})'.format(
            self.__class__.__name__, ProName.__str__(self),
            ProType.__str__(self), SchemaContainer.__str__(self),
            TemplateContainer.__str__(self)
        )
