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
    Defines unit tests for application Service class.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from gen_py_tool.core.model.project_setup import ProjectSetup
from gen_py_tool.core.service.engine import Service
from gen_py_tool.core.service.isubprocessor import ISubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestService(TestCase):
    '''
        Defines unit tests for application Service class.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validation for subprocessor.
                | test_execute_success - Verifies execute delegates to subprocessor.
                | test_execute_validation - Verifies execute validates params.
                | test_is_initialized - Verifies initialization state delegation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validation for subprocessor.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ValueError):
            Service(subprocessor=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(TypeError):
            Service(subprocessor=invalid_type)  # type: ignore[arg-type]

    def test_execute_success(self) -> None:
        '''
            Verifies execute delegates to subprocessor.

            :exceptions: None.
        '''
        mock_subprocessor: Mock = Mock(spec=ISubProcessor)
        mock_subprocessor.run.return_value = {'returncode': 0, 'stdout': 'ok', 'stderr': ''}

        service: Service = Service(subprocessor=mock_subprocessor)
        params: ProjectSetup = ProjectSetup(name='my_tool', output='./demo')
        result: Mapping[str, object] = service.execute(params=params)

        self.assertEqual(result['returncode'], 0)
        mock_subprocessor.run.assert_called_once_with(params=params)

    def test_execute_validation(self) -> None:
        '''
            Verifies execute validates params.

            :exceptions: None.
        '''
        service: Service = Service(subprocessor=Mock(spec=ISubProcessor))
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ValueError):
            service.execute(params=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(TypeError):
            service.execute(params=invalid_type)  # type: ignore[arg-type]

    def test_is_initialized(self) -> None:
        '''
            Verifies initialization state delegation.

            :exceptions: None.
        '''
        mock_subprocessor: Mock = Mock(spec=ISubProcessor)
        mock_subprocessor.is_initialized.return_value = True

        service: Service = Service(subprocessor=mock_subprocessor)
        self.assertTrue(service.is_initialized())


if __name__ == '__main__':
    main()

