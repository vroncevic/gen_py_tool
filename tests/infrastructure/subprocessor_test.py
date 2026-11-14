# -*- coding: UTF-8 -*-

'''
Module
    subprocessor_test.py
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
    Defines unit tests for SubProcessor adapter.
'''

from __future__ import annotations

from collections.abc import Mapping
from os import makedirs
from os.path import join
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.infrastructure.subprocessor import SubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSubProcessor(TestCase):
    '''
        Defines unit tests for SubProcessor adapter.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates generator.
                | test_run_success - Verifies template generation and file logging.
                | test_run_failures - Verifies unsuccessful generation and exception handling.
                | test_state_and_str - Verifies is_initialized and string representation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates generator.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            SubProcessor(generator=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            SubProcessor(generator=invalid_type)  # type: ignore[arg-type]

    def test_run_success(self) -> None:
        '''
            Verifies template generation and file logging.

            :exceptions: None.
        '''
        mock_logger: Mock = Mock(spec=ILogger)
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=mock_logger)
        mock_generator.generate.return_value = True

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)

        with TemporaryDirectory() as tmp_dir:
            with open(join(tmp_dir, 'main.py'), 'w', encoding='utf-8') as root_file:
                root_file.write('# root\n')

            sub_dir: str = join(tmp_dir, 'pkg')
            makedirs(sub_dir, exist_ok=True)
            with open(join(sub_dir, 'mod.py'), 'w', encoding='utf-8') as nested_file:
                nested_file.write('# nested\n')

            result: Mapping[str, object] = subprocessor.run(
                params=ProjectSetup(name='demo_tool', output=tmp_dir)
            )

        self.assertEqual(result['returncode'], 0)
        self.assertIn('demo_tool', str(result['stdout']))
        self.assertGreaterEqual(mock_logger.write_log.call_count, 3)

    def test_run_failures(self) -> None:
        '''
            Verifies unsuccessful generation and exception handling.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.generate.return_value = False

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)
        failed: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(name='demo_tool', output='./out')
        )
        self.assertEqual(failed['returncode'], 1)
        self.assertIn('failed to generate demo_tool', str(failed['stderr']))

        invalid_none: object = None
        exc_result: Mapping[str, object] = subprocessor.run(params=invalid_none)  # type: ignore[arg-type]
        self.assertEqual(exc_result['returncode'], 1)

    def test_state_and_str(self) -> None:
        '''
            Verifies is_initialized and string representation.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.is_initialized.return_value = True

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)
        self.assertTrue(subprocessor.is_initialized())
        self.assertIsInstance(str(subprocessor), str)


if __name__ == '__main__':
    main()

