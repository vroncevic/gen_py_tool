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
    Defines application service orchestrating Python tool generation.
'''

from __future__ import annotations

from collections.abc import Mapping

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.isubprocessor import ISubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class Service:
    '''
        Defines class Service implementing IService contract structurally.
        Orchestrates the Python tool project generation process.

        It defines:

            :attributes:
                | _subprocessor - Driven port adapter for subprocessing.
            :methods:
                | __init__ - Initializes Service constructor.
                | execute - Executes Python tool generation use case.
                | is_initialized - Checks if the service is initialized.
    '''

    _subprocessor: ISubProcessor[ProjectSetup, Mapping[str, object]]

    def __init__(self, subprocessor: ISubProcessor[ProjectSetup, Mapping[str, object]]) -> None:
        '''
            Initializes Service constructor.

            :param subprocessor: Driven port adapter for subprocessing.
            :exceptions:
                | ValueError: If subprocessor is not provided.
                | TypeError: If subprocessor does not satisfy ISubProcessor.
        '''
        ctx: str = 'service::init(...)'
        msg_subprocessor_none: str = 'the subprocessor must be provided'
        msg_subprocessor_istype: str = f'the subprocessor must be of type {ISubProcessor.__name__}'

        if subprocessor is None:
            raise ValueError(f'{ctx} - {msg_subprocessor_none}')

        if not isinstance(subprocessor, ISubProcessor):
            raise TypeError(f'{ctx} - {msg_subprocessor_istype}')

        self._subprocessor = subprocessor

    def execute(self, *, params: ProjectSetup) -> Mapping[str, object]:
        '''
            Executes Python tool generation use case.

            :param params: ProjectSetup domain configuration object.
            :return: Mapping containing returncode, stdout, and stderr.
            :exceptions:
                | ValueError: If params is not provided.
                | TypeError: If params is not an instance of ProjectSetup.
        '''
        ctx: str = 'service::execute(...)'
        msg_params_none: str = 'the params must be provided'
        msg_params_istype: str = f'the params must be of type {ProjectSetup.__name__}'

        if params is None:
            raise ValueError(f'{ctx} - {msg_params_none}')

        if not isinstance(params, ProjectSetup):
            raise TypeError(f'{ctx} - {msg_params_istype}')

        return self._subprocessor.run(params=params)

    def is_initialized(self) -> bool:
        '''
            Checks if the service is initialized.

            :return: True if the service is initialized, False otherwise.
            :exceptions: None.
        '''
        return self._subprocessor.is_initialized()

