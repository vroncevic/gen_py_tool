# -*- coding: UTF-8 -*-

'''
Module
    registry_test.py
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
    Defines unit tests for GenPyToolBundleRegistry class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.bundle import GenPyToolBundle
from gen_py_tool.setup.dependencies import GenPyToolBundleDependencies
from gen_py_tool.setup.registry import GenPyToolBundleRegistry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleRegistry(TestCase):
    '''
        Defines unit tests for GenPyToolBundleRegistry class.

        It defines:

            :methods:
                | test_create_bundle - Verifies registry creates validated GenPyToolBundle.
                | test_get_version - Verifies registry version string.
    '''

    def test_create_bundle(self) -> None:
        '''
            Verifies registry creates validated GenPyToolBundle.

            :exceptions: None.
        '''
        bundle: GenPyToolBundle = GenPyToolBundleRegistry.create_bundle(
            dependencies=GenPyToolBundleDependencies(
                base=Mock(spec=BaseBundle),
                service=Mock(spec=IService),
                subprocessor=Mock(spec=ISubProcessor),
                cli=Mock(spec=ICLI)
            )
        )
        self.assertIsInstance(bundle, GenPyToolBundle)

    def test_get_version(self) -> None:
        '''
            Verifies registry version string.

            :exceptions: None.
        '''
        self.assertEqual(GenPyToolBundleRegistry.get_version(), '1.4.2')


if __name__ == '__main__':
    main()

