# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Registry assembling and validating GenPyToolBundle instances.
'''

from __future__ import annotations

from gen_py_tool.setup.bundle import GenPyToolBundle
from gen_py_tool.setup.dep_validator import GenPyToolBundleDependenciesValidator
from gen_py_tool.setup.dependencies import GenPyToolBundleDependencies
from gen_py_tool.setup.keys import GenPyToolBundleKeys
from gen_py_tool.setup.validator import GenPyToolBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyToolBundleRegistry:
    '''
        Registry assembling and validating GenPyToolBundle instances.

        It defines:

            :methods:
                | create_bundle - Creates a validated GenPyToolBundle from dependencies.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenPyToolBundleDependencies) -> GenPyToolBundle:
        '''
            Creates a validated GenPyToolBundle from dependencies.

            :param dependencies: GenPyTool bundle dependencies.
            :return: Validated GenPyToolBundle instance.
            :exceptions:
                | ATSValueError: If dependencies or bundle values are missing.
                | ATSTypeError: If dependencies or bundle types are invalid.
        '''
        GenPyToolBundleDependenciesValidator.validate(dependencies)

        bundle: GenPyToolBundle = GenPyToolBundle(
            base=dependencies[GenPyToolBundleKeys.DEPENDENCY_BASE],
            service=dependencies[GenPyToolBundleKeys.DEPENDENCY_SERVICE],
            subprocessor=dependencies[GenPyToolBundleKeys.DEPENDENCY_SUBPROCESSOR],
            cli=dependencies[GenPyToolBundleKeys.DEPENDENCY_CLI]
        )

        GenPyToolBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: Registry version string.
            :exceptions: None.
        '''
        return __version__

