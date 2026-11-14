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
    Defines unit tests for GenPyToolBundleValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.bundle import GenPyToolBundle
from gen_py_tool.setup.validator import GenPyToolBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleValidator(TestCase):
    '''
        Defines unit tests for GenPyToolBundleValidator class.

        It defines:

            :methods:
                | test_valid_bundle - Verifies valid GenPyToolBundle passes validation.
                | test_invalid_bundle - Verifies invalid GenPyToolBundle fails validation.
    '''

    def test_valid_bundle(self) -> None:
        '''
            Verifies valid GenPyToolBundle passes validation.

            :exceptions: None.
        '''
        bundle: GenPyToolBundle = GenPyToolBundle(
            base=Mock(spec=BaseBundle),
            service=Mock(spec=IService),
            subprocessor=Mock(spec=ISubProcessor),
            cli=Mock(spec=ICLI)
        )
        GenPyToolBundleValidator.validate(bundle)
        self.assertTrue(GenPyToolBundleValidator.is_valid(bundle))

    def test_invalid_bundle(self) -> None:
        '''
            Verifies invalid GenPyToolBundle fails validation.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            GenPyToolBundleValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenPyToolBundleValidator.validate(invalid_type)  # type: ignore[arg-type]

        self.assertFalse(GenPyToolBundleValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

