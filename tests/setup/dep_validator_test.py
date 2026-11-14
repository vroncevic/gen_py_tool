# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Defines unit tests for GenPyToolBundleDependenciesValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.dep_validator import GenPyToolBundleDependenciesValidator
from gen_py_tool.setup.dependencies import GenPyToolBundleDependencies

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenPyToolBundleDependenciesValidator(TestCase):
    '''
        Defines unit tests for GenPyToolBundleDependenciesValidator class.

        It defines:

            :methods:
                | test_valid_dependencies - Verifies valid dependencies pass validation.
                | test_invalid_dependencies - Verifies invalid dependencies fail validation.
    '''

    def test_valid_dependencies(self) -> None:
        '''
            Verifies valid dependencies pass validation.

            :exceptions: None.
        '''
        dependencies: GenPyToolBundleDependencies = GenPyToolBundleDependencies(
            base=Mock(spec=BaseBundle),
            service=Mock(spec=IService),
            subprocessor=Mock(spec=ISubProcessor),
            cli=Mock(spec=ICLI)
        )
        GenPyToolBundleDependenciesValidator.validate(dependencies)
        self.assertTrue(GenPyToolBundleDependenciesValidator.is_valid(dependencies))

    def test_invalid_dependencies(self) -> None:
        '''
            Verifies invalid dependencies fail validation.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_entry: object = {
            'base': 'bad',
            'service': Mock(spec=IService),
            'subprocessor': Mock(spec=ISubProcessor),
            'cli': Mock(spec=ICLI)
        }

        with self.assertRaises(ATSValueError):
            GenPyToolBundleDependenciesValidator.validate(invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenPyToolBundleDependenciesValidator.validate(invalid_entry)  # type: ignore[arg-type]

        self.assertFalse(GenPyToolBundleDependenciesValidator.is_valid(invalid_none))  # type: ignore[arg-type]


if __name__ == '__main__':
    main()

