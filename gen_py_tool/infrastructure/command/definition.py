# -*- coding: UTF-8 -*-

'''
Module
    definition.py
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
    Defines CommandDefinition class for CLI create command metadata.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import ClassVar

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CommandDefinition:
    '''
        Defines class CommandDefinition implementing ICommandDefinition contract structurally.
        CLI subcommand metadata definition for Python tool project generation.

        It defines:

            :attributes:
                | COMMAND_NAME - CLI subcommand name.
                | HELP_TEXT - CLI subcommand help description.
                | DEFAULT_NAME - Default project name option value.
                | DEFAULT_OUTPUT - Default output directory option value.
            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns CommandDefinition string representation.
    '''

    COMMAND_NAME: ClassVar[str] = 'create'
    HELP_TEXT: ClassVar[str] = 'Generate Python tool project files'
    DEFAULT_NAME: ClassVar[str] = 'my_tool'
    DEFAULT_OUTPUT: ClassVar[str] = './'

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: Command name string.
            :exceptions: None.
        '''
        return self.COMMAND_NAME

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: Command help text string.
            :exceptions: None.
        '''
        return self.HELP_TEXT

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of OptionData definitions.
            :exceptions: None.
        '''
        return (
            OptionData(
                name='--name',
                help_text='Python tool project name',
                action=None,
                default=self.DEFAULT_NAME,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name='--output',
                help_text='Path to the output directory',
                action=None,
                default=self.DEFAULT_OUTPUT,
                required=True,
                choices=None,
                nargs=None
            ),
        )

    def __str__(self) -> str:
        '''
            Returns CommandDefinition string representation.

            :return: String representation of CommandDefinition.
            :exceptions: None.
        '''
        return to_str(self)

