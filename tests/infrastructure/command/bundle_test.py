# -*- coding: UTF-8 -*-

'''
Module
    bundle_test.py
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
    Defines unit tests for CommandBundle dataclass.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from gen_py_tool.infrastructure.command.bundle import CommandBundle
from gen_py_tool.infrastructure.command.definition import CommandDefinition
from gen_py_tool.infrastructure.command.executor import CommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCommandBundle(TestCase):
    '''
        Defines unit tests for CommandBundle dataclass.

        It defines:

            :methods:
                | test_create_bundle - Verifies CommandBundle holds definition and executor.
                | test_immutability - Verifies CommandBundle is frozen.
    '''

    def test_create_bundle(self) -> None:
        '''
            Verifies CommandBundle holds definition and executor.

            :exceptions: None.
        '''
        definition: CommandDefinition = CommandDefinition()
        executor: CommandExecutor = CommandExecutor(definition=definition)
        bundle: CommandBundle = CommandBundle(definition=definition, executor=executor)

        self.assertIs(bundle.definition, definition)
        self.assertIs(bundle.executor, executor)

    def test_immutability(self) -> None:
        '''
            Verifies CommandBundle is frozen.

            :exceptions: None.
        '''
        definition: CommandDefinition = CommandDefinition()
        bundle: CommandBundle = CommandBundle(
            definition=definition,
            executor=CommandExecutor(definition=definition)
        )
        with self.assertRaises(FrozenInstanceError):
            setattr(bundle, 'definition', definition)


if __name__ == '__main__':
    main()

