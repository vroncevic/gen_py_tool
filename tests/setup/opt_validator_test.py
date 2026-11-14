# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
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
    Defines unit tests for GenPyToolBundleOptionsValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_tool.setup.opt_validator import GenPyToolBundleOptionsValidator
from gen_py_tool.setup.options import GenPyToolBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleOptionsValidator(TestCase):
    '''
        Defines unit tests for GenPyToolBundleOptionsValidator class.

        It defines:

            :methods:
                | test_valid_options - Verifies valid options pass validation.
                | test_invalid_options - Verifies invalid options fail validation.
    '''

    def test_valid_options(self) -> None:
        '''
            Verifies valid options pass validation.

            :exceptions: None.
        '''
        options: GenPyToolBundleOptions = GenPyToolBundleOptions(info_file='gen_py_tool.cfg')
        GenPyToolBundleOptionsValidator.validate(options)
        self.assertTrue(GenPyToolBundleOptionsValidator.is_valid(options))

    def test_invalid_options(self) -> None:
        '''
            Verifies invalid options fail validation.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_entry: object = {'info_file': 123}

        with self.assertRaises(ATSValueError):
            GenPyToolBundleOptionsValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenPyToolBundleOptionsValidator.validate(invalid_entry)  # type: ignore[arg-type]

        self.assertFalse(GenPyToolBundleOptionsValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

