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
    Defines the CLIBundle dataclass.
'''

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from ats_utilities.option.imanager import IOptionManager
from ats_utilities.utils.reflection import instance_to_dict

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.command.bundle import CommandBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(slots=True, frozen=True, kw_only=True)
class CLIBundle:
    '''
        Defines the CLI component bundle.

        It defines:

            :attributes:
                | service - Service orchestrating project generation.
                | parser - Argument parser managing CLI options and subcommands.
                | commands - Immutable tuple of command definition/executor bundles.
            :methods:
                | to_dict - Converts the CLI bundle to a dictionary.
    '''

    service: IService[ProjectSetup, Mapping[str, object]]
    parser: IOptionManager
    commands: tuple[CommandBundle, ...]

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the CLI bundle to a dictionary.

            :return: Dictionary representation of the CLI bundle.
            :exceptions: None.
        '''
        return instance_to_dict(self)

