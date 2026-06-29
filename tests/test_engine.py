# -*- coding: UTF-8 -*-

'''
Module
    test_engine.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Unit tests for main engine (GenPyTool).
'''

import unittest
from unittest.mock import MagicMock, patch, call
from gen_py_tool.engine import GenPyTool
from gen_py_tool.gen_py_tool_bundle import GenPyToolBundle
from gen_py_tool.domain.ports.isubprocessor import ISubProcessor
from gen_py_tool.domain.ports.iservice import IService
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.generator.igenerator import IGenerator
from gen_py_tool.infrastructure.icli import ICLI

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestEngine(unittest.TestCase):
    '''
        Defines engine unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_default_init - Tests default constructor initialization.
                | test_custom_injection - Tests custom dependency injection in GenPyTool.
                | test_init_failure - Tests engine behavior when dependency initialization fails.
                | test_gen_py_tool_bundle_helpers - Tests GenPyToolBundle helpers.
                | test_init_failure_with_unexpected_exception - Tests engine behavior when dependency initialization fails with unexpected exception.
                | test_process_success - Tests that process() executes CLI if initialized.
                | test_process_failure - Tests that process() prints error and does not execute if uninitialized.
                | test_process_failure_with_unexpected_exception - Tests that process() prints error and does not execute if unexpected exception.
                | test_process_with_cli_error - Tests that process() handles CLI execution failure.
    '''

    def test_default_init(self) -> None:
        '''
            Tests default constructor initialization of GenPyTool.

            :exceptions: None.
        '''
        engine: GenPyTool = GenPyTool()
        self.assertTrue(engine._is_initialized)
        self.assertIsNotNone(engine._cli)

    def test_custom_injection(self) -> None:
        '''
            Tests custom dependency injection in GenPyTool constructor.

            :exceptions: None.
        '''
        mock_subprocessor: MagicMock = MagicMock(spec=ISubProcessor)
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_cli: MagicMock = MagicMock(spec=ICLI)

        bundle: GenPyToolBundle = GenPyToolBundle(
            subprocessor=mock_subprocessor,
            service=mock_service,
            parser=mock_parser,
            cli=mock_cli
        )

        engine: GenPyTool = GenPyTool(bundle)
        self.assertTrue(engine._is_initialized)
        self.assertEqual(engine._cli, mock_cli)

    def test_not_initialized_engine(self) -> None:
        '''
            Tests not initialized engine.

            :exceptions: None.
        '''
        with patch.object(GenPyTool, "_info_file", "invalid/path/gen_py_tool.cfg"):
            engine: GenPyTool = GenPyTool()
            self.assertFalse(engine._is_initialized)

    def test_init_failure(self) -> None:
        '''
            Tests engine behavior when dependency initialization fails.

            :exceptions: None.
        '''
        error_message: str = "Service initialization failed"

        with patch('gen_py_tool.engine.Service', side_effect=ATSValueError(error_message)):
            with patch('builtins.print') as mock_print:
                engine: GenPyTool = GenPyTool()
                self.assertFalse(engine._is_initialized)
                mock_print.assert_called_with(f'\x1b[31m❌ gen_py_tool: {error_message}\x1b[0m')

    def test_process_failure_with_unexpected_exception(self) -> None:
        '''
            Tests that process() prints error and does not execute if unexpected exception.

            :exceptions: None.
        '''
        with patch('gen_py_tool.engine.Service', side_effect=RuntimeError("unexpected error.")):
            with patch('builtins.print') as mock_print:
                engine: GenPyTool = GenPyTool()
                engine.process()
                mock_print.assert_any_call(f'\x1b[31m❌ gen_py_tool unexpected exception: unexpected error.\x1b[0m')

    def test_process_success(self) -> None:
        '''
            Tests that process() executes CLI if initialized.

            :exceptions: None.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.run.return_value = {"returncode": 0, "stdout": "ok", "stderr": ""}
        bundle: GenPyToolBundle = GenPyToolBundle(cli=mock_cli)

        engine: GenPyTool = GenPyTool(bundle)
        self.assertTrue(engine._is_initialized)

        engine.process()
        mock_cli.run.assert_called_once()

    def test_process_with_cli_error(self) -> None:
        '''
            Tests that process() handles CLI execution failure.

            :exceptions: None.
        '''
        mock_cli: MagicMock = MagicMock(spec=ICLI)
        mock_cli.run.return_value = {"returncode": 1, "stdout": "", "stderr": "CLI error"}
        bundle: GenPyToolBundle = GenPyToolBundle(cli=mock_cli)

        engine: GenPyTool = GenPyTool(bundle)
        self.assertTrue(engine._is_initialized)

        with patch('builtins.print') as mock_print:
            engine.process()
            mock_print.assert_any_call('\x1b[31m❌ gen_py_tool: CLI error\x1b[0m')
            mock_print.assert_any_call('\x1b[31m❌ gen_py_tool: exiting with error.\x1b[0m')

    def test_process_failure(self) -> None:
        '''
            Tests that process() prints error and does not execute if uninitialized.

            :exceptions: None.
        '''
        with patch('gen_py_tool.engine.Service', side_effect=ATSValueError("Service initialization failed")):
            with patch('builtins.print') as mock_print:
                engine: GenPyTool = GenPyTool()
                self.assertFalse(engine._is_initialized)

                engine.process()
                mock_print.assert_has_calls([
                    call('\x1b[31m❌ gen_py_tool: Service initialization failed\x1b[0m'),
                    call('\x1b[31m❌ gen_py_tool: engine not initialized.\x1b[0m')
                ])

    def test_gen_py_tool_bundle_helpers(self) -> None:
        '''
            Tests GenPyToolBundle merge and to_dict helpers.

            :exceptions: None.
        '''
        generator1: MagicMock = MagicMock(spec=IGenerator)
        subprocessor1: MagicMock = MagicMock(spec=ISubProcessor)
        service1: MagicMock = MagicMock(spec=IService)
        parser1: MagicMock = MagicMock(spec=IOptionManager)
        cli1: MagicMock = MagicMock(spec=ICLI)

        bundle1: GenPyToolBundle = GenPyToolBundle(subprocessor=subprocessor1, service=None)

        bundle2: GenPyToolBundle = GenPyToolBundle(subprocessor=None, service=service1)
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.subprocessor, subprocessor1)

        d = bundle1.to_dict()
        self.assertEqual(d["subprocessor"], subprocessor1)

        # Missing generator (generator=None)
        bundle3: GenPyToolBundle = GenPyToolBundle(
            generator=None, subprocessor=subprocessor1, service=service1, parser=parser1, cli=cli1
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle3.validate()
        self.assertEqual(str(ctx.exception), 'generator must be provided.')

        # Missing subprocessor (subprocessor=None)
        bundle4: GenPyToolBundle = GenPyToolBundle(
            generator=generator1, subprocessor=None, service=service1, parser=parser1, cli=cli1
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle4.validate()
        self.assertEqual(str(ctx.exception), 'subprocessor must be provided.')

        # Missing service (service=None)
        bundle5: GenPyToolBundle = GenPyToolBundle(
            generator=generator1, subprocessor=subprocessor1, service=None, parser=parser1, cli=cli1
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle5.validate()
        self.assertEqual(str(ctx.exception), 'service must be provided.')

        # Missing parser (parser=None)
        bundle6: GenPyToolBundle = GenPyToolBundle(
            generator=generator1, subprocessor=subprocessor1, service=service1, parser=None, cli=cli1
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle6.validate()
        self.assertEqual(str(ctx.exception), 'parser must be provided.')

        # Missing cli (cli=None)
        bundle7: GenPyToolBundle = GenPyToolBundle(
            generator=generator1, subprocessor=subprocessor1, service=service1, parser=parser1, cli=None
        )
        with self.assertRaises(ATSValueError) as ctx:
            bundle7.validate()
        self.assertEqual(str(ctx.exception), 'cli must be provided.')

        # All valid
        bundle8: GenPyToolBundle = GenPyToolBundle(
            generator=generator1, subprocessor=subprocessor1, service=service1, parser=parser1, cli=cli1
        )
        # Should not raise any exception
        bundle8.validate()
