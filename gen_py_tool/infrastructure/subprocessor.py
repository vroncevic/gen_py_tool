# -*- coding: UTF-8 -*-

'''
Module
    subprocessor.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines sub-processor adapter implementing ISubProcessor.
'''

from typing import Any, override
from os import walk
from os.path import dirname, realpath, relpath
from ats_utilities.generator.igenerator import IGenerator
from ats_utilities.generator.generator_bundle import GeneratorBundle
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.factory_class import format_instance_to_string
from gen_py_tool.domain.ports.isubprocessor import ISubProcessor

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class SubProcessor(ISubProcessor):
    '''
        Adapter that executes sub-processes.

        It defines:

            :attributes:
                | _scheme - Path to the scheme json file.
                | _templates - Path to the templates tgz file.
                | _generator - Generator adapter used to generate code from templates.
            :methods:
                | run - Executes a sub-process.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns the SubProcessor as string representation.
    '''

    _scheme: str = 'config/scheme.json'
    _templates: str = 'config/templates.tgz'

    def __init__(self, generator: IGenerator) -> None:
        '''
            Initializes the SubProcessor adapter.

            :param generator: Generator adapter.
            :type generator: <IGenerator>
            :exceptions:
                | ATSValueError - If the generator is not provided.
        '''
        if not generator:
            raise ATSValueError('generator must be provided.')

        self._generator = generator

    @override
    def run(self, params: dict[str, Any]) -> dict[str, Any]:
        '''
            Executes a sub-process.

            :param params: The command parameters to execute.
            :type params: <dict[str, Any]>
            :exceptions: None.
        '''
        current_dir: str = dirname(realpath(__file__))
        output_dir: str = params.get('output')
        template_key: str = params.get('type')
        project_name: str = params.get('name')
        scheme: str = f'{current_dir}/{self._scheme}'
        templates: str = f'{current_dir}/{self._templates}'

        success = self._generator.generate(
            GeneratorBundle(
                archive_path=templates,
                target_dir=output_dir,
                template_key=template_key,
                scheme=scheme,
                template_values={'project_name': project_name}
            )
        )

        if success:
            print("Generated files:")
            for root, dirs, files in walk(output_dir):
                for file in files:
                    rel_dir = relpath(root, output_dir)
                    if rel_dir == '.':
                        print(f"  {file}")
                    else:
                        print(f"  {rel_dir}/{file}")

        return {
            "returncode": 0 if success else 1,
            "stdout": 'successfully generated.' if success else '',
            "stderr": 'failed to generate.' if not success else ''
        }

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if the subprocessor is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._generator.is_initialized()

    @override
    def __str__(self) -> str:
        '''
            Returns the SubProcessor as string representation.

            :return: The SubProcessor as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
