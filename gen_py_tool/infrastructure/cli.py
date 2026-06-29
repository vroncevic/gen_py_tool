# -*- coding: UTF-8 -*-

'''
Module
    cli.py
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
    Defines CLI class implementing inbound CLI port.
'''

from typing import override
from ats_utilities.option.ioption_parser import IOptionManager
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_py_tool.infrastructure.icli import ICLI
from gen_py_tool.infrastructure.cli_bundle import CLIBundle
from gen_py_tool.domain.ports.iservice import IService
from gen_py_tool.infrastructure.icli_command import ICLICommand

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CLI(ICLI):
    '''
        Adapter that implements CLI commands for the code generator.

        It defines:

            :attributes:
                | _service - File generation orchestrator service.
                | _parser - Argument parser for parsing CLI command args.
                | _commands - Map of command names to command instances.
            :methods:
                | __init__ - Initializes the CLI with service, parser and commands list.
                | run - Parses command line arguments and runs selected command strategy.
                | is_initialized - Checks if the CLI component is initialized.
                | __str__ - Returns the CLI as string representation.
    '''

    def __init__(self, component_bundle: CLIBundle | None = None):
        '''
            Initializes the CLI with service, parser and commands list.

            :param component_bundle: Bundle containing CLI adapters | None.
            :type component_bundle: <CLIBundle | None>
            :exceptions:
                | ATSValueError: Component bundle (CLIBundle) must be provided.
        '''
        if component_bundle is None:
            raise ATSValueError("component bundle (CLIBundle) must be provided.")

        component_bundle.validate()
        self._service: IService = component_bundle.service
        self._parser: IOptionManager = component_bundle.parser
        self._commands: dict[str, ICLICommand] = {cmd.name: cmd for cmd in component_bundle.commands}
        self._parser.register_commands(component_bundle.commands)

    @override
    def run(self) -> None:
        '''
            Parses command line arguments and runs selected command strategy.

            :exceptions:
                | SystemExit: Parser exits after successful argument parsing or on error.
                | OSError: OS-related errors during command execution.
        '''
        command_name, params = self._parser.parse_command()
        cmd: ICLICommand = self._commands.get(command_name)

        if cmd:
            cmd.execute(params, self._service)

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the file writer component is initialized.

            :return: True (success) | False (fail).
            :rtype: <bool>
            :exceptions: None.
        '''
        return True

    @override
    def __str__(self) -> str:
        '''
            Returns the CLI as string representation.

            :return: The CLI as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
