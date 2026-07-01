# -*- coding: UTF-8 -*-

'''
Module
    test_domain.py
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
    Unit tests for domain models.
'''

import unittest
from typing import Any
from gen_py_tool.domain.models import Tool

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.1'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class TestDomain(unittest.TestCase):
    '''
        Defines domain unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_from_params_success - Tests successful creation of Tool from parameters.
                | test_from_params_missing_arguments - Tests that missing arguments raises ValueError.
    '''

    def test_from_params_success(self) -> None:
        '''
            Tests successful creation of Tool from parameters.

            :exceptions: None.
        '''
        params: dict[str, Any] = {'name': 'test', 'tool': 'tool_standalone', 'output': './'}
        tool: Tool = Tool.from_params(params=params)

        self.assertIsNotNone(tool.params)
        self.assertEqual(tool.params['name'], 'test')
        self.assertEqual(tool.params['tool'], 'tool_standalone')
        self.assertEqual(tool.params['output'], './')

    def test_from_params_missing_arguments(self) -> None:
        '''
            Tests that missing arguments raises ATSValueError.

            :exceptions: None.
        '''
        params: dict[str, Any] = None

        with self.assertRaises(ValueError):
            Tool.from_params(params=params)
