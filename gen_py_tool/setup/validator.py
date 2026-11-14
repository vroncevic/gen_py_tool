# -*- coding: UTF-8 -*-

'''
Module
    validator.py
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
    Validator for GenPyToolBundle instances.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_py_tool.core.service.iservice import IService
from gen_py_tool.core.service.isubprocessor import ISubProcessor
from gen_py_tool.infrastructure.cli.icli import ICLI
from gen_py_tool.setup.bundle import GenPyToolBundle

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyToolBundleValidator:
    '''
        Validator for GenPyToolBundle instances.

        It defines:

            :methods:
                | validate - Validates the GenPyTool bundle.
                | is_valid - Checks if the GenPyTool bundle is valid.
    '''

    @classmethod
    def validate(cls, bundle: GenPyToolBundle) -> None:
        '''
            Validates the GenPyTool bundle.

            :param bundle: GenPyTool bundle to validate.
            :exceptions:
                | ATSValueError: If bundle or any attribute is None.
                | ATSTypeError: If bundle or any attribute has invalid type.
        '''
        ctx: str = 'gen_py_tool_bundle_validator::validate(...)'
        not_none(bundle, ctx, 'the gen_py_tool bundle must be provided')
        istype(bundle, GenPyToolBundle, ctx, 'the gen_py_tool bundle must be an instance of GenPyToolBundle')

        not_none(bundle.base, ctx, 'the base bundle must be provided')
        not_none(bundle.service, ctx, 'the service must be provided')
        not_none(bundle.subprocessor, ctx, 'the subprocessor must be provided')
        not_none(bundle.cli, ctx, 'the cli must be provided')

        istype(bundle.base, BaseBundle, ctx, 'the base bundle must be an instance of BaseBundle')
        istype(bundle.service, IService, ctx, 'the service must be an instance of IService')
        istype(bundle.subprocessor, ISubProcessor, ctx, 'the subprocessor must be an instance of ISubProcessor')
        istype(bundle.cli, ICLI, ctx, 'the cli must be an instance of ICLI')

    @classmethod
    def is_valid(cls, bundle: GenPyToolBundle) -> bool:
        '''
            Checks if the GenPyTool bundle is valid.

            :param bundle: GenPyTool bundle to check.
            :return: True if valid, False otherwise.
            :exceptions: None.
        '''
        try:
            cls.validate(bundle)
            return True
        except (ATSValueError, ATSTypeError):
            return False

