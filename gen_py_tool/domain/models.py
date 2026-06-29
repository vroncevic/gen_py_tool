# -*- coding: UTF-8 -*-

'''
Module
    models.py
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
    Defines domain modes representing tool parameters.
'''

from dataclasses import dataclass
from typing import Any
from ats_utilities.exceptions.ats_value_error import ATSValueError

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


@dataclass
class Tool:
    '''
        Domain model representing a tool.

        It defines:

            :attributes:
                | params - The dict of parameters for the tool.
            :methods:
                | from_params - Factory method that constructs Tool with parameters.
    '''

    params: dict[str, Any]

    @classmethod
    def from_params(cls, params: dict[str, Any]) -> "Tool":
        '''
            Factory method that constructs Tool with parameters.

            :param params: Parameters for the tool.
            :type params: <dict[str, Any]>
            :return: The generated Tool domain model instance with tool parameters.
            :rtype: <Tool>
            :exceptions:
                | ATSValueError: Tool parameters must be provided.
        '''
        if not params:
            raise ATSValueError("tool parameters dict must be provided.")

        return cls(params=params)
