# -*- coding: UTF-8 -*-

'''
Module
    ping_command.py
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
    Defines CreateCommand class implementing ICLICommand strategy.
'''

from typing import Any, override
from ats_utilities.factory_class import format_instance_to_string
from ats_utilities.option.command_option import CommandOption
from ats_utilities.exceptions.ats_value_error import ATSValueError
from gen_py_tool.infrastructure.icli_command import ICLICommand
from gen_py_tool.domain.ports.iservice import IService

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class CreateCommand(ICLICommand):
    '''
        CLI subcommand for generating a Python project (Tool or Generator).

        It defines:

            :attributes: None.
            :methods:
                | name - Returns the command name key.
                | help_text - Returns the command help text.
                | options - Returns the list of command options.
                | to_tool_args - Converts the subcommand parameters to tool arguments.
                | execute - Executes the subcommand.
                | __str__ - Returns the CreateCommand as string representation.
    '''

    @property
    @override
    def name(self) -> str:
        '''
            Returns the command name key.

            :return: The command name key.
            :rtype: <str>
            :exceptions: None.
        '''
        return "create"

    @property
    @override
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: The command help text.
            :rtype: <str>
            :exceptions: None.
        '''
        return "Generate Python Tool/Generator project"

    @property
    @override
    def options(self) -> list[CommandOption]:
        '''
            Returns the command options.

            :return: List of command options.
            :rtype: <list[CommandOption]>
            :exceptions: None.
        '''
        return [
            CommandOption(
                name="--name",
                help_text="Python Tool/Generator project name",
                default="mytool",
                required=True
            ),
            CommandOption(
                name="--type",
                help_text="Python Tool/Generator project type",
                default="tool",
                required=True
            ),
            CommandOption(
                name="--output",
                help_text="Path to the output directory",
                default="./",
                required=True
            )
        ]

    def to_tool_args(self, params: dict[str, Any]) -> dict[str, Any]:
        '''
            Converts subcommand parameters to the tool arguments.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :return: The dictionary of tool arguments.
            :rtype: <dict[str, Any]>
            :exceptions:
                | ATSValueError: Params must be provided.
        '''
        if not params:
            raise ATSValueError("params must be provided.")

        param_mapping: dict[str, str] = {
            "tool": "tool_standalone",
            "tool_ats": "tool_with_ats_utilities",
            "gen": "generator_standalone",
            "gen_ats": "gen_with_ats_utilities"
        }
        new_cli_params: dict[str, Any] = {}

        for key, value in params.items():
            if key == 'type':
                new_cli_params[key] = param_mapping.get(value)
            else:
                new_cli_params[key] = value

        return new_cli_params

    @override
    def execute(self, params: dict[str, Any], service: IService) -> None:
        '''
            Executes the subcommand.

            :param params: Subcommand parameters from CLI parser.
            :type params: <dict[str, Any]>
            :param service: Command orchestrator service instance.
            :type service: <IService>
            :exceptions: None.
        '''
        print(f"🔥 Executing {self.name} command...")
        service.execute(params=self.to_tool_args(params))
        print(f"✅ Executed {self.name} command.")

    @override
    def __str__(self) -> str:
        '''
            Returns the CreateCommand as string representation.

            :return: The CreateCommand as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
