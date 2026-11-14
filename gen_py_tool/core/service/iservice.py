# -*- coding: UTF-8 -*-

'''
Module
    iservice.py
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
    Defines structural interface for application services.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class IService[ServiceParamsType, ExecuteResultType](Protocol):
    '''
        Defines structural interface for application services.

        It defines:

            :methods:
                | execute - Executes the service use case.
                | is_initialized - Checks if the service is initialized.
    '''

    def execute(self, *, params: ServiceParamsType) -> ExecuteResultType:
        '''
            Executes the service use case.

            :param params: Parameters for the service execution.
            :return: Result of the execution.
        '''

    def is_initialized(self) -> bool:
        '''
            Checks if the service is initialized.

            :return: True if the service is initialized, False otherwise.
        '''

