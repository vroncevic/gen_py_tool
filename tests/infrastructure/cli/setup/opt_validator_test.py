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
    Defines unit tests for CLIBundleOptionsValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.infrastructure.cli.setup.opt_validator import CLIBundleOptionsValidator
from gen_py_tool.infrastructure.cli.setup.options import CLIBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleOptionsValidator(TestCase):
    '''
        Defines unit tests for CLIBundleOptionsValidator class.

        It defines:

            :methods:
                | test_valid_options - Verifies valid options pass validate and is_valid.
                | test_invalid_options - Verifies invalid options fail validation.
    '''

    def test_valid_options(self) -> None:
        '''
            Verifies valid options pass validate and is_valid.

            :exceptions: None.
        '''
        options: CLIBundleOptions = CLIBundleOptions(
            service=Mock(spec=IService),
            parser=Mock(spec=IOptionManager)
        )
        CLIBundleOptionsValidator.validate(options)
        self.assertTrue(CLIBundleOptionsValidator.is_valid(options))

    def test_invalid_options(self) -> None:
        '''
            Verifies invalid options fail validation.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_entry: object = {'service': 'bad', 'parser': Mock(spec=IOptionManager)}

        with self.assertRaises(ATSValueError):
            CLIBundleOptionsValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CLIBundleOptionsValidator.validate(invalid_entry)  # type: ignore[arg-type]

        self.assertFalse(CLIBundleOptionsValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

