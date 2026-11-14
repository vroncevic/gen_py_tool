# -*- coding: UTF-8 -*-

'''
Module
    iexecutor_test.py
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
    Defines unit tests for ICommandExecutor structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_py_tool.infrastructure.command.definition import CommandDefinition
from gen_py_tool.infrastructure.command.executor import CommandExecutor
from gen_py_tool.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestICommandExecutor(TestCase):
    '''
        Defines unit tests for ICommandExecutor structural protocol.

        It defines:

            :methods:
                | test_structural_conformance - Verifies CommandExecutor satisfies ICommandExecutor.
                | test_non_conformance - Verifies plain object does not satisfy ICommandExecutor.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies CommandExecutor satisfies ICommandExecutor.

            :exceptions: None.
        '''
        executor: CommandExecutor = CommandExecutor(definition=CommandDefinition())
        self.assertIsInstance(executor, ICommandExecutor)

    def test_non_conformance(self) -> None:
        '''
            Verifies plain object does not satisfy ICommandExecutor.

            :exceptions: None.
        '''
        self.assertNotIsInstance(object(), ICommandExecutor)


if __name__ == '__main__':
    main()

