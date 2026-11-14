# -*- coding: UTF-8 -*-

'''
Module
    validator_test.py
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
    Defines unit tests for CLIBundleValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.validator import CLIBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleValidator(TestCase):
    '''
        Defines unit tests for CLIBundleValidator class.

        It defines:

            :methods:
                | test_valid_bundle - Verifies valid CLIBundle passes validation.
                | test_invalid_bundle - Verifies invalid CLIBundle fails validation.
    '''

    def test_valid_bundle(self) -> None:
        '''
            Verifies valid CLIBundle passes validation.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundle(
            service=Mock(spec=IService),
            parser=Mock(spec=IOptionManager),
            commands=()
        )
        CLIBundleValidator.validate(bundle)
        self.assertTrue(CLIBundleValidator.is_valid(bundle))

    def test_invalid_bundle(self) -> None:
        '''
            Verifies invalid CLIBundle fails validation.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            CLIBundleValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CLIBundleValidator.validate(invalid_type)  # type: ignore[arg-type]

        self.assertFalse(CLIBundleValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

