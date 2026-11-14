# -*- coding: UTF-8 -*-

'''
Module
    idefinition.py
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
    Defines structural ICommandDefinition strategy interface.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from ats_utilities.option.command.ioption import IOption

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ICommandDefinition(Protocol):
    '''
        Defines structural ICommandDefinition strategy interface.

        It defines:

            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of options for the command.
                | __str__ - Returns string representation of command definition.
    '''

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: Command subcommand name.
        '''

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: Command help text string.
        '''

    @property
    def options(self) -> Sequence[IOption]:
        '''
            Returns the sequence of options for the command.

            :return: Sequence of command option definitions.
        '''

    def __str__(self) -> str:
        '''
            Returns string representation of command definition.

            :return: String representation.
        '''

