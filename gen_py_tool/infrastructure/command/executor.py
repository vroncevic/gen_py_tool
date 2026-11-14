# -*- coding: UTF-8 -*-

'''
Module
    executor.py
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
    Defines CommandExecutor class executing the CLI create command.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.command.idefinition import ICommandDefinition

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CommandExecutor:
    '''
        Defines class CommandExecutor implementing ICommandExecutor contract structurally.
        Command executor strategy for generating Python tool project files.

        It defines:

            :attributes:
                | _definition - Command CLI metadata definition.
            :methods:
                | __init__ - Initializes CommandExecutor constructor.
                | execute - Executes the create subcommand.
                | get_definition - Returns the command definition metadata.
                | __str__ - Returns CommandExecutor string representation.
    '''

    _definition: ICommandDefinition

    def __init__(self, definition: ICommandDefinition) -> None:
        '''
            Initializes CommandExecutor constructor.

            :param definition: Command definition metadata.
            :exceptions:
                | ATSValueError: If definition is None.
                | ATSTypeError: If definition does not satisfy ICommandDefinition.
        '''
        ctx: str = 'command_executor::init(...)'
        not_none(definition, ctx, 'the definition must be provided')
        istype(definition, ICommandDefinition, ctx, f'the definition must be an instance of {ICommandDefinition.__name__}')
        self._definition = definition

    def execute(
        self,
        *,
        params: Mapping[str, object],
        service: IService[ProjectSetup, Mapping[str, object]]
    ) -> Mapping[str, object]:
        '''
            Executes the create subcommand.

            :param params: Subcommand parameters parsed from CLI.
            :param service: Application service orchestrator instance.
            :return: Mapping containing returncode, stdout, and stderr.
            :exceptions: None.
        '''
        if not service.is_initialized():
            return {'returncode': 1, 'stdout': '', 'stderr': 'service not initialized'}

        setup: ProjectSetup = ProjectSetup(
            name=str(params.get('name', '')),
            output=str(params.get('output', ''))
        )
        return service.execute(params=setup)

    def get_definition(self) -> ICommandDefinition:
        '''
            Returns the command definition metadata.

            :return: Command definition metadata.
            :exceptions: None.
        '''
        return self._definition

    def __str__(self) -> str:
        '''
            Returns CommandExecutor string representation.

            :return: String representation of CommandExecutor.
            :exceptions: None.
        '''
        return to_str(self)

