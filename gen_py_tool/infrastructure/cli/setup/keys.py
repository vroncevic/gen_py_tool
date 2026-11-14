# -*- coding: UTF-8 -*-

'''
Module
    keys.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines runtime keys and type mappings for the CLI bundle.
'''

from __future__ import annotations

from collections.abc import Sequence
from types import MappingProxyType
from typing import ClassVar

from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleKeys:
    '''
        Runtime component keys and interface constraints for the CLI bundle.

        It defines:

            :attributes:
                | DEPENDENCY_SERVICE - Service interface key of the CLI bundle.
                | DEPENDENCY_PARSER - Parser interface key of the CLI bundle.
                | DEPENDENCY_COMMANDS - Commands sequence key of the CLI bundle.
                | OPTION_SERVICE - Service option key of the CLI bundle.
                | OPTION_PARSER - Parser option key of the CLI bundle.
            :methods:
                | get_dependency_to_type - Returns mapping of CLI bundle dependencies to types.
                | get_option_to_type - Returns mapping of CLI bundle options to types.
    '''

    DEPENDENCY_SERVICE: ClassVar[str] = 'service'
    DEPENDENCY_PARSER: ClassVar[str] = 'parser'
    DEPENDENCY_COMMANDS: ClassVar[str] = 'commands'

    OPTION_SERVICE: ClassVar[str] = 'service'
    OPTION_PARSER: ClassVar[str] = 'parser'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of CLI bundle dependencies to types.

            :return: Immutable mapping of dependency keys to expected types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_SERVICE: IService,
            cls.DEPENDENCY_PARSER: IOptionManager,
            cls.DEPENDENCY_COMMANDS: Sequence,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of CLI bundle options to types.

            :return: Immutable mapping of option keys to expected types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.OPTION_SERVICE: IService,
            cls.OPTION_PARSER: IOptionManager,
        })

