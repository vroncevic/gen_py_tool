# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the CLIBundle.
'''

from __future__ import annotations

from gen_py_tool.infrastructure.cli.setup.bundle import CLIBundle
from gen_py_tool.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_py_tool.infrastructure.cli.setup.keys import CLIBundleKeys
from gen_py_tool.infrastructure.cli.setup.opt_validator import CLIBundleOptionsValidator
from gen_py_tool.infrastructure.cli.setup.options import CLIBundleOptions
from gen_py_tool.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_py_tool.infrastructure.command.bundle import CommandBundle
from gen_py_tool.infrastructure.command.definition import CommandDefinition
from gen_py_tool.infrastructure.command.executor import CommandExecutor
from gen_py_tool.infrastructure.command.idefinition import ICommandDefinition

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleFactory:
    '''
        Factory for creating the CLIBundle.

        It defines:

            :methods:
                | create_bundle - Creates the CLI bundle from pre-configured options.
                | get_version - Returns the factory version.
    '''

    @classmethod
    def create_bundle(cls, options: CLIBundleOptions) -> CLIBundle:
        '''
            Creates the CLI bundle from pre-configured options.

            :param options: CLI bundle options containing service and parser.
            :return: Validated CLIBundle instance.
            :exceptions:
                | ATSValueError: If options or dependencies are missing.
                | ATSTypeError: If options or dependencies have invalid types.
        '''
        CLIBundleOptionsValidator.validate(options)

        create_definition: ICommandDefinition = CommandDefinition()
        create_cmd: CommandBundle = CommandBundle(
            definition=create_definition,
            executor=CommandExecutor(definition=create_definition)
        )

        return CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=options[CLIBundleKeys.OPTION_SERVICE],
                parser=options[CLIBundleKeys.OPTION_PARSER],
                commands=(create_cmd,)
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: Factory version string.
            :exceptions: None.
        '''
        return __version__

