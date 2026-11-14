# -*- coding: UTF-8 -*-

'''
Module
    dep_validator.py
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
    Validator for GenPyToolBundleDependencies.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_py_tool.setup.dependencies import GenPyToolBundleDependencies
from gen_py_tool.setup.keys import GenPyToolBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyToolBundleDependenciesValidator:
    '''
        Validator for GenPyToolBundleDependencies.

        It defines:

            :methods:
                | validate - Validates GenPyTool bundle dependencies.
                | is_valid - Checks if GenPyTool bundle dependencies are valid.
    '''

    @classmethod
    def validate(cls, dependencies: GenPyToolBundleDependencies) -> None:
        '''
            Validates GenPyTool bundle dependencies.

            :param dependencies: Bundle dependencies to validate.
            :exceptions:
                | ATSValueError: If dependencies or any required entry is None.
                | ATSTypeError: If dependencies or any entry has invalid type.
        '''
        ctx: str = 'gen_py_tool_bundle_dependencies_validator::validate(...)'
        not_none(dependencies, ctx, 'the gen_py_tool bundle dependencies must be provided')
        istype(dependencies, Mapping, ctx, 'the gen_py_tool bundle dependencies must be a Mapping')

        for attr_name, expected_type in GenPyToolBundleKeys.get_dependency_to_type().items():
            label: str = attr_name.replace('_', ' ')
            attribute: object = dependencies.get(attr_name)
            not_none(attribute, ctx, f'the {label} must be provided')
            istype(attribute, expected_type, ctx, f'the {label} must be an instance of {expected_type.__name__}')

    @classmethod
    def is_valid(cls, dependencies: GenPyToolBundleDependencies) -> bool:
        '''
            Checks if GenPyTool bundle dependencies are valid.

            :param dependencies: Bundle dependencies to check.
            :return: True if valid, False otherwise.
            :exceptions: None.
        '''
        try:
            cls.validate(dependencies)
            return True
        except (ATSValueError, ATSTypeError):
            return False

