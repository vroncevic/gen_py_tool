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
    Defines unit tests for CLIBundleRegistry class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_py_tool.infrastructure.cli.setup.registry import CLIBundleRegistry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleRegistry(TestCase):
    '''
        Defines unit tests for CLIBundleRegistry class.

        It defines:

            :methods:
                | test_create_bundle - Verifies registry creates validated CLIBundle.
                | test_get_version - Verifies registry version string.
    '''

    def test_create_bundle(self) -> None:
        '''
            Verifies registry creates validated CLIBundle.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=Mock(spec=IService),
                parser=Mock(spec=IOptionManager),
                commands=()
            )
        )
        self.assertIsInstance(bundle, CLIBundle)

    def test_get_version(self) -> None:
        '''
            Verifies registry version string.

            :exceptions: None.
        '''
        self.assertEqual(CLIBundleRegistry.get_version(), '1.4.2')


if __name__ == '__main__':
    main()

