# -*- coding: UTF-8 -*-

'''
Module
    executor_test.py
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
    Defines unit tests for CommandExecutor class.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.iservice import IService
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


class TestCommandExecutor(TestCase):
    '''
        Defines unit tests for CommandExecutor class.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates definition.
                | test_execute_success - Verifies execute calls initialized service.
                | test_execute_uninitialized_service - Verifies failure when service is uninitialized.
                | test_definition_and_str - Verifies get_definition and string representation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates definition.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            CommandExecutor(definition=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CommandExecutor(definition=invalid_type)  # type: ignore[arg-type]

    def test_execute_success(self) -> None:
        '''
            Verifies execute calls initialized service.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0, 'stdout': 'done', 'stderr': ''}

        executor: CommandExecutor = CommandExecutor(definition=CommandDefinition())
        result: Mapping[str, object] = executor.execute(
            params={'name': 'my_tool', 'output': './demo'},
            service=mock_service
        )

        self.assertEqual(result['returncode'], 0)
        mock_service.execute.assert_called_once_with(
            params=ProjectSetup(name='my_tool', output='./demo')
        )

    def test_execute_uninitialized_service(self) -> None:
        '''
            Verifies failure when service is uninitialized.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_service.is_initialized.return_value = False

        executor: CommandExecutor = CommandExecutor(definition=CommandDefinition())
        result: Mapping[str, object] = executor.execute(params={}, service=mock_service)

        self.assertEqual(result['returncode'], 1)
        self.assertEqual(result['stderr'], 'service not initialized')

    def test_definition_and_str(self) -> None:
        '''
            Verifies get_definition and string representation.

            :exceptions: None.
        '''
        definition: CommandDefinition = CommandDefinition()
        executor: CommandExecutor = CommandExecutor(definition=definition)

        self.assertIs(executor.get_definition(), definition)
        self.assertIsInstance(str(executor), str)


if __name__ == '__main__':
    main()

