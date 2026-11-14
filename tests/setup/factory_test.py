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
    Defines unit tests for GenPyToolBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_py_tool.setup.bundle import GenPyToolBundle
from gen_py_tool.setup.factory import GenPyToolBundleFactory
from gen_py_tool.setup.options import GenPyToolBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleFactory(TestCase):
    '''
        Defines unit tests for GenPyToolBundleFactory class.

        It defines:

            :methods:
                | test_create_bundle_default - Verifies default GenPyToolBundle creation.
                | test_create_bundle_with_options - Verifies GenPyToolBundle creation with explicit options.
                | test_get_version - Verifies factory version string.
    '''

    def test_create_bundle_default(self) -> None:
        '''
            Verifies default GenPyToolBundle creation.

            :exceptions: None.
        '''
        bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenPyToolBundle)

    def test_create_bundle_with_options(self) -> None:
        '''
            Verifies GenPyToolBundle creation with explicit options.

            :exceptions: None.
        '''
        bundle: GenPyToolBundle = GenPyToolBundleFactory.create_bundle(
            options=GenPyToolBundleOptions(info_file=GenPyToolBundleFactory.DEFAULT_INFO_FILE)
        )
        self.assertIsInstance(bundle, GenPyToolBundle)

    def test_get_version(self) -> None:
        '''
            Verifies factory version string.

            :exceptions: None.
        '''
        self.assertEqual(GenPyToolBundleFactory.get_version(), '1.4.2')


if __name__ == '__main__':
    main()

