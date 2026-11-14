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
    Runtime component keys and interface constraints for GenPyToolBundle.
'''

from __future__ import annotations

from types import MappingProxyType
from typing import ClassVar

from ats_utilities.base.setup.bundle import BaseBundle

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyToolBundleKeys:
    '''
        Runtime component keys and interface constraints for GenPyToolBundle.

        It defines:

            :attributes:
                | DEPENDENCY_BASE - Base bundle dependency key.
                | DEPENDENCY_SERVICE - Service dependency key.
                | DEPENDENCY_SUBPROCESSOR - SubProcessor dependency key.
                | DEPENDENCY_CLI - CLI dependency key.
                | OPTION_INFO_FILE - Info file path option key.
            :methods:
                | get_dependency_to_type - Returns mapping of bundle dependencies to types.
                | get_option_to_type - Returns mapping of bundle options to types.
    '''

    DEPENDENCY_BASE: ClassVar[str] = 'base'
    DEPENDENCY_SERVICE: ClassVar[str] = 'service'
    DEPENDENCY_SUBPROCESSOR: ClassVar[str] = 'subprocessor'
    DEPENDENCY_CLI: ClassVar[str] = 'cli'

    OPTION_INFO_FILE: ClassVar[str] = 'info_file'

    @classmethod
    def get_dependency_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of bundle dependencies to types.

            :return: Immutable mapping of dependency keys to expected types.
            :exceptions: None.
        '''
        return MappingProxyType({
            cls.DEPENDENCY_BASE: BaseBundle,
            cls.DEPENDENCY_SERVICE: IService,
            cls.DEPENDENCY_SUBPROCESSOR: ISubProcessor,
            cls.DEPENDENCY_CLI: ICLI,
        })

    @classmethod
    def get_option_to_type(cls) -> MappingProxyType[str, type]:
        '''
            Returns mapping of bundle options to types.

            :return: Immutable mapping of option keys to expected types.
            :exceptions: None.
        '''
        return MappingProxyType({cls.OPTION_INFO_FILE: str})

