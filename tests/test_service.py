# -*- coding: UTF-8 -*-

'''
Module
    test_service.py
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
    Unit tests for application service.
'''

import unittest
from unittest.mock import MagicMock, patch
from typing import Any
from gen_py_tool.domain.ports.isubprocessor import ISubProcessor
from gen_py_tool.application.service import Service

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class MockSubProcessor(ISubProcessor):
    '''
        Mock class for testing purpose

        It defines:

            :attributes:
                | return_value - The value returned by the run method.
                | called_with - The arguments with which the run method was called.
            :methods:
                | __init__ - Initializes the mock subprocessor.
                | run - Runs a command.
    '''
    def __init__(self, return_value: dict[str, Any] = None) -> None:
        '''
            Initializes the mock subprocessor.

            :param return_value: The value returned by the run method.
            :raises None.
        '''
        self.return_value: dict[str, Any] = return_value if return_value is not None else {
            "stdout": "", "stderr": "", "returncode": 0
        }
        self.called_with: list[dict[str, Any]] = []

    def run(self, command: list[str], capture_output: bool = False, text: bool = True) -> dict[str, Any]:
        '''
            Runs a command.

            :param command: The command to run.
            :param capture_output: Whether to capture the output.
            :param text: Whether to decode the output as text.
            :raises None.
        '''
        self.called_with.append({
            "command": command,
            "capture_output": capture_output,
            "text": text
        })
        return self.return_value

    def is_initialized(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"MockSubProcessor {self.return_value}"


class TestService(unittest.TestCase):
    '''
        Defines application service unit tests.

        It defines:

            :attributes: None
            :methods:
                | test_init_success - Tests successful service initialization.
                | test_init_missing_subprocessor - Tests initialization fails when subprocessor is None.
                | test_execute_success - Tests successful service execution.
                | test_execute_raises_exception - Tests that Service raises exception when subprocessor raises exception.
                | test_execute_missing_args - Tests execution fails when arguments are missing.
                | test_execute_with_non_zero_return_code - Tests execution fails when subprocessor returns non-zero return code.
    '''

    def test_init_success(self) -> None:
        '''
            Tests successful service initialization with a valid subprocessor.

            :raises None.
        '''
        mock_subprocessor: MockSubProcessor = MockSubProcessor(return_value={"stdout": "hello", "stderr": "", "returncode": 0})
        service: Service = Service(subprocessor=mock_subprocessor)
        self.assertIsNotNone(service)

        with patch('builtins.print') as mock_print:
            service.execute(["echo", "hello"])
            mock_print.assert_called_with("hello")

        self.assertEqual(mock_subprocessor.called_with[0]["command"], ["echo", "hello"])
        self.assertTrue(mock_subprocessor.called_with[0]["capture_output"])
        self.assertTrue(mock_subprocessor.called_with[0]["text"])

        self.assertTrue(isinstance(str(service), str))
        self.assertNotEqual(str(service), "")

    def test_init_missing_subprocessor(self) -> None:
        '''
            Tests initialization fails when subprocessor is None.

            :raises ValueError: When subprocessor is None.
        '''
        with self.assertRaises(ValueError):
            Service(None)

    def test_execute_raises_exception(self) -> None:
        '''
            Tests that Service raises exception when subprocessor raises exception.

            :raises Exception: When subprocessor raises exception.
        '''
        mock_response: dict[str, Any] = {"stdout": "Success!", "stderr": "", "returncode": 0}
        mock_processor: MockSubProcessor = MockSubProcessor(return_value=mock_response)
        mock_processor.run = MagicMock(side_effect=Exception("Test exception"))
        service: Service = Service(subprocessor=mock_processor)

        with self.assertRaises(Exception):
            service.execute(["echo", "hello"])

    def test_execute_missing_args(self) -> None:
        '''
            Tests execution fails when params is None.

            :raises ValueError: When params is None.
        '''
        mock_response: dict[str, Any] = {"stdout": "Success!", "stderr": "", "returncode": 0}
        mock_processor: MockSubProcessor = MockSubProcessor(return_value=mock_response)
        service: Service = Service(subprocessor=mock_processor)

        with self.assertRaises(ValueError):
            service.execute(None)

    def test_execute_with_non_zero_return_code(self) -> None:
        '''
            Tests execution fails when subprocessor returns non-zero return code.

            :raises ValueError: When subprocessor returns non-zero return code.
        '''
        mock_response: dict[str, Any] = {"stdout": "", "stderr": "Error!", "returncode": 1}
        mock_processor: MockSubProcessor = MockSubProcessor(return_value=mock_response)
        service: Service = Service(subprocessor=mock_processor)

        with patch('builtins.print') as mock_print:
            service.execute(["echo", "hello"])
            mock_print.assert_called_with("Error!")
