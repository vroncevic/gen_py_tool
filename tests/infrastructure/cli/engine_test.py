# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Defines unit tests for CLI inbound adapter.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.engine import CLI
from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.command.bundle import CommandBundle
from gen_py_tool.infrastructure.command.definition import CommandDefinition
from gen_py_tool.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLI(TestCase):
    '''
        Defines unit tests for CLI inbound adapter.

        It defines:

            :methods:
                | test_run_success - Verifies CLI dispatches parsed command to executor.
                | test_run_command_not_found - Verifies CLI returns error for unknown command.
                | test_run_exception - Verifies CLI catches ATS exceptions during parsing.
                | test_state_and_str - Verifies is_initialized and string representation.
    '''

    def test_run_success(self) -> None:
        '''
            Verifies CLI dispatches parsed command to executor.

            :exceptions: None.
        '''
        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.return_value = ('create', {'name': 'my_tool', 'output': './demo'})

        mock_executor: Mock = Mock(spec=ICommandExecutor)
        mock_executor.execute.return_value = {'returncode': 0, 'stdout': 'ok', 'stderr': ''}

        cli: CLI = CLI(
            CLIBundle(
                service=Mock(spec=IService),
                parser=mock_parser,
                commands=(CommandBundle(definition=CommandDefinition(), executor=mock_executor),)
            )
        )
        result: Mapping[str, object] = cli.run()

        self.assertEqual(result['returncode'], 0)
        mock_executor.execute.assert_called_once()

    def test_run_command_not_found(self) -> None:
        '''
            Verifies CLI returns error for unknown command.

            :exceptions: None.
        '''
        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.return_value = ('unknown', {})

        cli: CLI = CLI(
            CLIBundle(service=Mock(spec=IService), parser=mock_parser, commands=())
        )
        result: Mapping[str, object] = cli.run()

        self.assertEqual(result['returncode'], 1)
        self.assertIn('command not found', str(result['stderr']))

    def test_run_exception(self) -> None:
        '''
            Verifies CLI catches ATS exceptions during parsing.

            :exceptions: None.
        '''
        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.side_effect = ATSValueError('parse failure')

        cli: CLI = CLI(
            CLIBundle(service=Mock(spec=IService), parser=mock_parser, commands=())
        )
        result: Mapping[str, object] = cli.run()

        self.assertEqual(result['returncode'], 1)
        self.assertIn('cli::run -', str(result['stderr']))

    def test_state_and_str(self) -> None:
        '''
            Verifies is_initialized and string representation.

            :exceptions: None.
        '''
        cli: CLI = CLI(
            CLIBundle(
                service=Mock(spec=IService),
                parser=Mock(spec=IOptionManager),
                commands=()
            )
        )
        self.assertTrue(cli.is_initialized())
        self.assertIsInstance(str(cli), str)


if __name__ == '__main__':
    main()

