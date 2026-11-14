# -*- coding: UTF-8 -*-

'''
Module
    dependencies_test.py
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
    Defines unit tests for GenPyToolBundleDependencies TypedDict.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.dependencies import GenPyToolBundleDependencies

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleDependencies(TestCase):
    '''
        Defines unit tests for GenPyToolBundleDependencies TypedDict.

        It defines:

            :methods:
                | test_dependencies_creation - Verifies GenPyToolBundleDependencies entries.
    '''

    def test_dependencies_creation(self) -> None:
        '''
            Verifies GenPyToolBundleDependencies entries.

            :exceptions: None.
        '''
        mock_base: Mock = Mock(spec=BaseBundle)
        mock_service: Mock = Mock(spec=IService)
        mock_subprocessor: Mock = Mock(spec=ISubProcessor)
        mock_cli: Mock = Mock(spec=ICLI)

        dependencies: GenPyToolBundleDependencies = GenPyToolBundleDependencies(
            base=mock_base,
            service=mock_service,
            subprocessor=mock_subprocessor,
            cli=mock_cli
        )

        self.assertIs(dependencies['base'], mock_base)
        self.assertIs(dependencies['service'], mock_service)
        self.assertIs(dependencies['subprocessor'], mock_subprocessor)
        self.assertIs(dependencies['cli'], mock_cli)


if __name__ == '__main__':
    main()

