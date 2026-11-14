# -*- coding: UTF-8 -*-

'''
Module
    isubprocessor_test.py
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
    Defines unit tests for ISubProcessor structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger

from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.subprocessor import SubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestISubProcessor(TestCase):
    '''
        Defines unit tests for ISubProcessor structural protocol.

        It defines:

            :methods:
                | test_structural_conformance - Verifies SubProcessor satisfies ISubProcessor.
                | test_non_conformance - Verifies plain object does not satisfy ISubProcessor.
    '''

    def test_structural_conformance(self) -> None:
        '''
            Verifies SubProcessor satisfies ISubProcessor.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))

        subprocessor: SubProcessor = SubProcessor(generator=mock_generator)
        self.assertIsInstance(subprocessor, ISubProcessor)

    def test_non_conformance(self) -> None:
        '''
            Verifies plain object does not satisfy ISubProcessor.

            :exceptions: None.
        '''
        self.assertNotIsInstance(object(), ISubProcessor)


if __name__ == '__main__':
    main()

