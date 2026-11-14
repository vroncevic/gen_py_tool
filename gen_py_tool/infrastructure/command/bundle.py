# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Defines CommandBundle dataclass combining command definition and executor.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.iservice import IService
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


@dataclass(slots=True, frozen=True)
class CommandBundle:
    '''
        Command bundle holding command definition and command executor.

        It defines:

            :attributes:
                | definition - Command CLI metadata definition.
                | executor - Command execution strategy.
    '''

    definition: ICommandDefinition
    executor: ICommandExecutor[
        ICommandDefinition,
        Mapping[str, object],
        Mapping[str, object],
        IService[ProjectSetup, Mapping[str, object]]
    ]

