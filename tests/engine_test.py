# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Defines unit tests for GenPyTool engine class.
'''

from __future__ import annotations

from io import StringIO
from unittest import TestCase, main
from unittest.mock import Mock, patch

from ats_utilities.exceptions import ATSValueError

from gen_py_tool.engine import GenPyTool
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.bundle import GenPyToolBundle
from gen_py_tool.setup.factory import GenPyToolBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyTool(TestCase):
    '''
        Defines unit tests for GenPyTool engine class.

        It defines:

            :methods:
                | test_init_success_and_failures - Verifies engine initialization and error branches.
                | test_process_success_and_cli_failure - Verifies process success and CLI failure returncode.
                | test_process_not_initialized - Verifies process returns False when uninitialized.
                | test_process_exceptions - Verifies process handles ATS and unexpected exceptions.
    '''

    def test_init_success_and_failures(self) -> None:
        '''
            Verifies engine initialization and error branches.

            :exceptions: None.
        '''
        valid_bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle()
        engine: GenPyTool = GenPyTool(valid_bundle)
        self.assertTrue(engine.is_initialized())

        invalid_none: object = None
        buffer: StringIO = StringIO()
        with patch('gen_py_tool.engine.stdout', buffer):
            uninit_engine: GenPyTool = GenPyTool(invalid_none)  # type: ignore[arg-type]
        self.assertFalse(uninit_engine.is_initialized())

        with patch(
            'gen_py_tool.engine.GenPyToolBundleValidator.validate',
            side_effect=RuntimeError('unexpected')
        ), patch('gen_py_tool.engine.stdout', buffer):
            err_engine: GenPyTool = GenPyTool(valid_bundle)
        self.assertFalse(err_engine.is_initialized())

    def test_process_success_and_cli_failure(self) -> None:
        '''
            Verifies process success and CLI failure returncode.

            :exceptions: None.
        '''
        default_bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle()
        mock_cli_ok: Mock = Mock(spec=ICLI)
        mock_cli_ok.is_initialized.return_value = True
        mock_cli_ok.run.return_value = {'returncode': 0, 'stdout': 'ok', 'stderr': ''}

        ok_engine: GenPyTool = GenPyTool(
            GenPyToolBundle(
                base=default_bundle.base,
                service=default_bundle.service,
                subprocessor=default_bundle.subprocessor,
                cli=mock_cli_ok
            )
        )
        self.assertTrue(ok_engine.process())

        mock_cli_fail: Mock = Mock(spec=ICLI)
        mock_cli_fail.is_initialized.return_value = True
        mock_cli_fail.run.return_value = {'returncode': 1, 'stdout': '', 'stderr': 'failed'}

        fail_engine: GenPyTool = GenPyTool(
            GenPyToolBundle(
                base=default_bundle.base,
                service=default_bundle.service,
                subprocessor=default_bundle.subprocessor,
                cli=mock_cli_fail
            )
        )
        self.assertFalse(fail_engine.process())

    def test_process_not_initialized(self) -> None:
        '''
            Verifies process returns False when uninitialized.

            :exceptions: None.
        '''
        default_bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle()
        mock_cli: Mock = Mock(spec=ICLI)
        mock_cli.is_initialized.return_value = False

        engine: GenPyTool = GenPyTool(
            GenPyToolBundle(
                base=default_bundle.base,
                service=default_bundle.service,
                subprocessor=default_bundle.subprocessor,
                cli=mock_cli
            )
        )
        buffer: StringIO = StringIO()
        with patch('gen_py_tool.engine.stdout', buffer):
            self.assertFalse(engine.process())

    def test_process_exceptions(self) -> None:
        '''
            Verifies process handles ATS and unexpected exceptions.

            :exceptions: None.
        '''
        default_bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle()
        mock_cli: Mock = Mock(spec=ICLI)
        mock_cli.is_initialized.return_value = True
        mock_cli.run.side_effect = ATSValueError('ats failure')

        engine: GenPyTool = GenPyTool(
            GenPyToolBundle(
                base=default_bundle.base,
                service=default_bundle.service,
                subprocessor=default_bundle.subprocessor,
                cli=mock_cli
            )
        )
        buffer: StringIO = StringIO()
        with patch('gen_py_tool.engine.stdout', buffer):
            self.assertFalse(engine.process())

        mock_cli.run.side_effect = RuntimeError('unexpected failure')
        with patch('gen_py_tool.engine.stdout', buffer):
            self.assertFalse(engine.process())


if __name__ == '__main__':
    main()

