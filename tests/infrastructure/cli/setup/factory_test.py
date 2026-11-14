# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Defines unit tests for CLIBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.factory import CLIBundleFactory
from gen_py_tool.infrastructure.cli.setup.options import CLIBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleFactory(TestCase):
    '''
        Defines unit tests for CLIBundleFactory class.

        It defines:

            :methods:
                | test_create_bundle - Verifies factory creates CLIBundle with create command.
                | test_get_version - Verifies factory version string.
    '''

    def test_create_bundle(self) -> None:
        '''
            Verifies factory creates CLIBundle with create command.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundleFactory.create_bundle(
            options=CLIBundleOptions(
                service=Mock(spec=IService),
                parser=Mock(spec=IOptionManager)
            )
        )
        self.assertIsInstance(bundle, CLIBundle)
        self.assertEqual(len(bundle.commands), 1)
        self.assertEqual(bundle.commands[0].definition.name, 'create')

    def test_get_version(self) -> None:
        '''
            Verifies factory version string.

            :exceptions: None.
        '''
        self.assertEqual(CLIBundleFactory.get_version(), '1.4.2')


if __name__ == '__main__':
    main()

