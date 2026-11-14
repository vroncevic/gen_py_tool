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
    Registry assembling and validating CLIBundle instances.
'''

from __future__ import annotations

from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.dep_validator import CLIBundleDependenciesValidator
from gen_py_tool.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_py_tool.infrastructure.cli.setup.keys import CLIBundleKeys
from gen_py_tool.infrastructure.cli.setup.validator import CLIBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleRegistry:
    '''
        Registry assembling and validating CLIBundle instances.

        It defines:

            :methods:
                | create_bundle - Creates a validated CLIBundle from dependencies.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: CLIBundleDependencies) -> CLIBundle:
        '''
            Creates a validated CLIBundle from dependencies.

            :param dependencies: CLI bundle dependencies.
            :return: Validated CLIBundle instance.
            :exceptions:
                | ATSValueError: If dependencies or resulting bundle values are missing.
                | ATSTypeError: If dependencies or resulting bundle types are invalid.
        '''
        CLIBundleDependenciesValidator.validate(dependencies)

        bundle: CLIBundle = CLIBundle(
            service=dependencies[CLIBundleKeys.DEPENDENCY_SERVICE],
            parser=dependencies[CLIBundleKeys.DEPENDENCY_PARSER],
            commands=tuple(dependencies[CLIBundleKeys.DEPENDENCY_COMMANDS])
        )

        CLIBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: Registry version string.
            :exceptions: None.
        '''
        return __version__

