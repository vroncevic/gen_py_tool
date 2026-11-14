# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Defines CLI class implementing inbound ICLI port structurally.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.exceptions import ATSRuntimeError, ATSTypeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager
from ats_utilities.utils.reflection import to_str

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.validator import CLIBundleValidator
from gen_py_tool.infrastructure.command.idefinition import ICommandDefinition
from gen_py_tool.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

type RegisteredExecutor = ICommandExecutor[
    ICommandDefinition,
    Mapping[str, object],
    Mapping[str, object],
    IService[ProjectSetup, Mapping[str, object]]
]


class CLI:
    '''
        Defines class CLI implementing ICLI contract structurally.
        Inbound adapter dispatching CLI subcommands to command executors.

        It defines:

            :attributes:
                | _service - Project generation orchestrator service.
                | _parser - Argument parser for CLI command options.
                | _executors - Mapping of command names to command executors.
            :methods:
                | __init__ - Initializes CLI with validated CLIBundle.
                | run - Parses CLI arguments and runs selected command strategy.
                | is_initialized - Checks if the CLI is initialized.
                | __str__ - Returns CLI string representation.
    '''

    _service: IService[ProjectSetup, Mapping[str, object]]
    _parser: IOptionManager
    _executors: Mapping[str, RegisteredExecutor]

    def __init__(self, bundle: CLIBundle) -> None:
        '''
            Initializes CLI with validated CLIBundle.

            :param bundle: Bundle containing CLI collaborators.
            :exceptions:
                | ATSValueError: If bundle or its attributes are None.
                | ATSTypeError: If bundle or its attributes have invalid types.
        '''
        CLIBundleValidator.validate(bundle)
        self._service = bundle.service
        self._parser = bundle.parser
        self._executors = {pair.definition.name: pair.executor for pair in bundle.commands}
        self._parser.register_commands([pair.definition for pair in bundle.commands])

    def run(self) -> Mapping[str, object]:
        '''
            Parses CLI arguments and runs selected command strategy.

            :return: Execution result mapping with returncode, stdout, and stderr.
            :exceptions: None.
        '''
        try:
            command_name, params = self._parser.parse_command()
            executor: RegisteredExecutor | None = self._executors.get(command_name)

            if executor is None:
                return {'returncode': 1, 'stdout': '', 'stderr': 'cli::run - command not found'}

            return executor.execute(params=params, service=self._service)

        except (ATSRuntimeError, ATSValueError, ATSTypeError) as exc:
            return {'returncode': 1, 'stdout': '', 'stderr': f'cli::run - {exc}'}

    def is_initialized(self) -> bool:
        '''
            Checks if the CLI is initialized.

            :return: True if CLI is initialized, False otherwise.
            :exceptions: None.
        '''
        return True

    def __str__(self) -> str:
        '''
            Returns CLI string representation.

            :return: String representation of CLI.
            :exceptions: None.
        '''
        return to_str(self)

