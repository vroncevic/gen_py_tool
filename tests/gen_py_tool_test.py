# -*- coding: UTF-8 -*-

'''
Module
    gen_py_tool_test.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class TestGenPyTool with attribute(s) and method(s).
    Creates test cases for checking functionalities of GenPyTool.
Execute
    python3 -m unittest -v gen_py_tool_test
'''

import sys
from typing import List
from unittest import TestCase, main

try:
    from gen_py_tool import GenPyTool
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_py_tool'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.3.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyTool(TestCase):
    '''
        Defines class TestGenPyTool with attribute(s) and method(s).
        Creates test cases for checking functionalities of GenPyTool.
        GenPyTool unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - Call before test case.
                | tearDown - Call after test case.
                | test_default_create - Default on create (not None).
                | test_missing_args - Test missing args.
                | test_missing_type - Test missing type.
                | test_process_tool - Test generation of tool structure.
                | test_process_gen - Test generation of generator structure.
    '''
    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_default_create(self) -> None:
        '''Default on create (not None)'''
        generator: GenPyTool = GenPyTool()
        self.assertIsNotNone(generator)

    def test_missing_args(self) -> None:
        '''Test missing args'''
        sys.argv.clear()
        generator: GenPyTool = GenPyTool()
        self.assertFalse(generator.process())

    def test_missing_type(self) -> None:
        '''Test missing type'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'mytool')
        generator: GenPyTool = GenPyTool()
        self.assertFalse(generator.process())

    def test_process_tool(self) -> None:
        '''Test generation of tool structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'mytool')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'tool')
        generator: GenPyTool = GenPyTool()
        self.assertTrue(generator.process())

    def test_process_gen(self) -> None:
        '''Test generation of generator structure'''
        sys.argv.clear()
        sys.argv.insert(0, '-n')
        sys.argv.insert(1, 'mygen')
        sys.argv.insert(2, '-t')
        sys.argv.insert(3, 'gen')
        generator: GenPyTool = GenPyTool()
        self.assertTrue(generator.process())


if __name__ == '__main__':
    main()
