# -*- coding: UTF-8 -*-

'''
Module
    test_infrastructure.py
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
    Unit tests for infrastructure adapters.
'''

import unittest
from unittest.mock import patch, MagicMock, call
from typing import Any
from ats_utilities.option.engine import OptionManager
from ats_utilities.option.component_bundle import OptionComponentBundle
from ats_utilities.context_bundle import ContextBundle
from ats_utilities.checker.engine import Checker
from ats_utilities.reporter.engine import Reporter
from ats_utilities.option.command_option import CommandOption
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_py_tool.infrastructure.icli_command import ICLICommand
from gen_py_tool.infrastructure.cli_bundle import CLIBundle
from gen_py_tool.infrastructure.cli import CLI
from gen_py_tool.infrastructure.create_command import CreateCommand
from gen_py_tool.domain.ports.iservice import IService
from gen_py_tool.domain.ports.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.subprocessor import SubProcessor
from ats_utilities.generator.igenerator import IGenerator

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class DummyCommand(ICLICommand):
    '''
        Dummy CLI command for testing ArgParser.

        It defines:

            :attributes: None.
            :methods:
                | name - Command name.
                | help_text - Command help text.
                | options - Command options.
                | execute - Simulates command execution.
    '''

    @property
    def name(self) -> str:
        '''
            Returns command name.

            :return: The command name.
            :rtype: <str>
            :exceptions: None.
        '''
        return "dummy"

    @property
    def help_text(self) -> str:
        '''
            Returns command help text.

            :return: The command help.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Dummy command for tests"

    @property
    def options(self) -> list[CommandOption]:
        '''
            Returns command options.

            :return: List of command options.
            :rtype: <List[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(name="--foo", help_text="foo parameter", default="bar"),
            CommandOption(name="--req", help_text="required parameter", required=True),
        ]

    def execute(self, params: dict, service: IService) -> None:
        '''
            Simulates execution.

            :param params: Execution params.
            :type params: <dict>
            :param service: Generation service.
            :type service: <IFileGen>
            :exceptions: None.
        '''
        pass

    def __str__(self) -> str:
        '''
            Returns the string representation of the command.

            :return: The string representation of the command.
            :rtype: <str>
            :exceptions: None.
        '''
        return f"DummyCommand(name='{self.name}', help_text='{self.help_text}', options={self.options})"


class TestInfrastructure(unittest.TestCase):
    '''
        Defines infrastructure adapters unit tests.

        It defines:

            :attributes: None.
            :methods:
                | test_arg_parser_success - Tests successful CLI argument parsing.
                | test_cli_bundle_validation - Tests validation checks of CLIBundle.
                | test_cli_run_executes_command - Tests that CLI.run executes matching command strategy.
                | test_gen_config_command_metadata - Tests GenConfigCommand properties.
                | test_gen_service_command_metadata - Tests GenServiceCommand properties.
                | test_cli_bundle_helpers - Tests CLIBundle helper methods.
                | test_cli_run_failure_with_unexpected_exception - Tests that CLI.run prints error and does not execute if unexpected exception.
                | test_cli_bundle_validate_commands_none - Tests CLIBundle validation with None commands.
                | test_cli_init_missing_bundle - Tests CLI init with None bundle.
                | test_init_failure_with_unexpected_exception - Tests engine behavior when dependency initialization fails with unexpected exception.
                | test_concrete_file_writer_read_failure - Tests file writing failure when underlying file system operation raises exception.
                | test_file_reader_not_found - Tests file reading with non-existing file.
                | test_concrete_template_provider - Tests concrete TemplateProvider.
                | test_concrete_subprocessor - Tests concrete SubProcessor.
                | test_subprocessor_execution_error - Tests SubProcessor execution error handling.
    '''

    def test_arg_parser_success(self) -> None:
        '''
            Tests successful registration and parsing of CLI arguments.

            :exceptions: None.
        '''
        context: ContextBundle = ContextBundle(checker=Checker(), reporter=Reporter(), verbose=False)
        params: dict[str, str] = {
            'ats_name': 'test_cli',
            'ats_version': '1.0.0',
            'ats_licence': 'MIT',
            'ats_build_date': '2026-06-22'
        }
        bundle: OptionComponentBundle = OptionComponentBundle(parameters=params, context_bundle=context)
        parser: OptionManager = OptionManager(bundle)

        cmd: DummyCommand = DummyCommand()
        parser.register_commands([cmd])

        test_args: list[str] = ["main.py", "dummy", "--req", "val", "--foo", "baz"]
        cmd_name: str
        params: dict[str, str]

        with patch("sys.argv", test_args):
            cmd_name, params = parser.parse_command()

        self.assertEqual(cmd_name, "dummy")
        self.assertEqual(params["req"], "val")
        self.assertEqual(params["foo"], "baz")

    def test_cli_bundle_validation(self) -> None:
        '''
            Tests validation checks of CLIBundle.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundle(service=None, parser=None, commands=None)
        with self.assertRaises(ValueError):
            bundle.validate()

        bundle_partial: CLIBundle = CLIBundle(service=MagicMock(), parser=None, commands=[])
        with self.assertRaises(ValueError):
            bundle_partial.validate()

    def test_cli_run_executes_command(self) -> None:
        '''
            Tests that CLI.run parses arguments and delegates execution to the matched command.

            :exceptions: None.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)
        mock_command: MagicMock = MagicMock(spec=ICLICommand)
        mock_command.name = "dummy"

        mock_parser.parse_command.return_value = ("dummy", {"foo": "bar"})

        cli_bundle: CLIBundle = CLIBundle(service=mock_service, parser=mock_parser, commands=[mock_command])
        cli: CLI = CLI(cli_bundle)
        cli.run()

        mock_parser.parse_command.assert_called_once()
        mock_command.execute.assert_called_once_with({"foo": "bar"}, mock_service)

        self.assertIsNotNone(str(cli))
        self.assertIsNotNone(repr(cli))
        self.assertIsInstance(str(cli), str)
        self.assertIsInstance(repr(cli), str)
        self.assertNotEqual(str(cli), "")
        self.assertNotEqual(repr(cli), "")

    def test_gen_config_command_metadata(self) -> None:
        '''
            Tests GenConfigCommand properties and parameter mapping execution.

            :exceptions: None.
        '''
        cmd: CreateCommand = CreateCommand()
        self.assertEqual(cmd.name, "create")
        self.assertEqual(cmd.help_text, "Generate Python Tool/Generator project")
        self.assertEqual(len(cmd.options), 3)
        self.assertIsNotNone(str(cmd))
        self.assertIsNotNone(repr(cmd))
        self.assertIsInstance(str(cmd), str)
        self.assertIsInstance(repr(cmd), str)
        self.assertNotEqual(str(cmd), "")
        self.assertNotEqual(repr(cmd), "")

        mock_service: MagicMock = MagicMock(spec=IService)
        params: dict[str, str] = {"name": "test", "type": "tool", "output": "./"}
        cmd.execute(params, mock_service)

        mock_service.execute.assert_called_once_with(
            params={"name": "test", "type": "tool_standalone", "output": "./"}
        )

    def test_cli_bundle_helpers(self) -> None:
        '''
            Tests CLIBundle helper methods (merge, to_dict).

            :exceptions: None.
        '''
        mock_service: MagicMock = MagicMock(spec=IService)
        mock_parser: MagicMock = MagicMock(spec=IOptionManager)

        bundle1: CLIBundle = CLIBundle(service=mock_service, parser=None, commands=None)
        bundle2: CLIBundle = CLIBundle(service=None, parser=mock_parser, commands=[])
        bundle1.merge(bundle2)

        self.assertEqual(bundle1.service, mock_service)
        self.assertEqual(bundle1.parser, mock_parser)
        self.assertEqual(bundle1.commands, [])

        d: dict[str, Any] = bundle1.to_dict()
        self.assertEqual(d["service"], mock_service)
        self.assertEqual(d["parser"], mock_parser)
        self.assertEqual(d["commands"], [])

    def test_cli_bundle_validate_commands_none(self) -> None:
        '''
            Tests CLIBundle validate raises ValueError when commands list is None.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundle(service=MagicMock(), parser=MagicMock(), commands=None)
        with self.assertRaises(ValueError):
            bundle.validate()

    def test_cli_init_missing_bundle(self) -> None:
        '''
            Tests CLI initialization raises ValueError when bundle is None.

            :exceptions: None.
        '''
        with self.assertRaises(ValueError):
            CLI(None)

    def test_command_option_init(self) -> None:
        '''
            Tests CommandOption initialization and attributes.

            :exceptions: None.
        '''
        opt: CommandOption = CommandOption(
            name="--test",
            help_text="Test description",
            default="default_val",
            required=True,
            choices=["choice1", "choice2"]
        )
        self.assertEqual(opt.name, "--test")
        self.assertEqual(opt.help_text, "Test description")
        self.assertEqual(opt.default, "default_val")
        self.assertTrue(opt.required)
        self.assertEqual(opt.choices, ["choice1", "choice2"])

class TestSubProcessor(unittest.TestCase):
    '''
        Defines unit tests for SubProcessor adapter to achieve 100% coverage.

        It defines:
            :methods:
                | test_run_success - Tests execution with successful generation.
                | test_run_failure - Tests execution with failing generation.
                | test_subprocessor_init_none - Tests initialization with None generator.
                | test_subprocessor_is_initialized - Tests is_initialized method.
                | test_subprocessor_str - Tests SubProcessor string representation.
    '''

    def test_run_success(self) -> None:
        '''
            Tests execution when generation succeeds.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_generator.generate.return_value = True
        
        subprocessor: ISubProcessor = SubProcessor(generator=mock_generator)
        params: dict[str, Any] = {'name': 'test', 'type': 'tool', 'output': './'}
        
        res: dict[str, Any] = subprocessor.run(params)

        self.assertEqual(res["returncode"], 0)
        self.assertEqual(res["stdout"], "successfully generated.")
        self.assertEqual(res["stderr"], "")
        mock_generator.generate.assert_called_once()

    def test_run_failure(self) -> None:
        '''
            Tests execution when generation fails.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_generator.generate.return_value = False
        
        subprocessor: ISubProcessor = SubProcessor(generator=mock_generator)
        params: dict[str, Any] = {'name': 'test', 'type': 'tool', 'output': './'}
        
        res: dict[str, Any] = subprocessor.run(params)

        self.assertEqual(res["returncode"], 1)
        self.assertEqual(res["stdout"], "")
        self.assertEqual(res["stderr"], "failed to generate.")
        mock_generator.generate.assert_called_once()

    def test_subprocessor_init_none(self) -> None:
        '''
            Tests that SubProcessor raises ATSValueError when generator is None.
        '''
        with self.assertRaises(ATSValueError):
            SubProcessor(None)

    def test_subprocessor_is_initialized(self) -> None:
        '''
            Tests is_initialized method delegates to generator.
        '''
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        mock_generator.is_initialized.return_value = True
        subprocessor: ISubProcessor = SubProcessor(generator=mock_generator)
        self.assertTrue(subprocessor.is_initialized())
        mock_generator.is_initialized.assert_called_once()

    def test_subprocessor_str(self) -> None:
        """
            Tests SubProcessor string representation.
        """
        mock_generator: MagicMock = MagicMock(spec=IGenerator)
        subprocessor: ISubProcessor = SubProcessor(generator=mock_generator)
        self.assertIsNotNone(str(subprocessor))
        self.assertIsInstance(str(subprocessor), str)
        self.assertNotEqual(str(subprocessor), "")

class TestPingCommand(unittest.TestCase):

    def setUp(self) -> None:
        self.command: ICLICommand = CreateCommand()

    def test_to_tool_args_with_none(self) -> None:
        """Cover branch where params is None."""
        with self.assertRaises(ATSValueError):
            self.command.to_tool_args(None)

    def test_to_tool_args_with_empty_dict(self) -> None:
        """Cover branch where params is an empty dict."""
        with self.assertRaises(ATSValueError):
            self.command.to_tool_args({})

    def test_to_tool_args_ignores_unknown_param(self) -> None:
        """Cover branch where key not in mapping."""
        result: dict[str, Any] = self.command.to_tool_args({
            "unknown": "value"
        })

        self.assertEqual(result, {"unknown": "value"})

    def test_to_tool_args_all_params(self) -> None:
        result: dict[str, Any] = self.command.to_tool_args({'name': 'test', 'type': 'tool', 'output': './'})

        self.assertEqual(
            result,
            {'name': 'test', 'type': 'tool_standalone', 'output': './'}
        )

    @patch("builtins.print")
    def test_execute(self, mock_print) -> None:
        service: MagicMock = MagicMock(spec=IService)

        self.command.execute(
            {'name': 'test', 'type': 'tool', 'output': './'},
            service
        )

        service.execute.assert_called_once_with(
            params={'name': 'test', 'type': 'tool_standalone', 'output': './'}
        )

        mock_print.assert_has_calls([
            call("🔥 Executing create command..."),
            call("✅ Executed create command.")
        ])

    @patch.object(CreateCommand, "to_tool_args")
    @patch("builtins.print")
    def test_execute_calls_to_tool_args(
        self,
        mock_print,
        mock_to_tool_args
    ) -> None:
        mock_to_tool_args.return_value = {
            'name': 'test',
            'type': 'tool_standalone',
            'output': './'
        }

        service: MagicMock = MagicMock(spec=IService)

        params: dict[str, Any] = {'name': 'test', 'type': 'tool', 'output': './'}

        self.command.execute(params, service)

        mock_to_tool_args.assert_called_once_with(params)

        service.execute.assert_called_once_with(
            params={'name': 'test', 'type': 'tool_standalone', 'output': './'}
        )
