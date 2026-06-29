# -*- coding: UTF-8 -*-

'''
Module
    service.py
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
    Service for orchestrating the tool execution process.
'''

from typing import Any, override
from ats_utilities.exceptions.ats_value_error import ATSValueError
from ats_utilities.factory_class import format_instance_to_string
from gen_py_tool.domain.ports.iservice import IService
from gen_py_tool.domain.ports.isubprocessor import ISubProcessor
from gen_py_tool.domain.models import Tool

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Development'


class Service(IService):
    '''
        Service for orchestrating the tool execution process.

        It defines:

            :attributes:
                | _subprocessor - Adapter for executing sub-processes.
            :methods:
                | __init__ - Initializes the Service.
                | execute - Executes a tool using the subprocessor adapter.
    '''

    def __init__(self, subprocessor: ISubProcessor) -> None:
        '''
            Initializes the Service.

            :param subprocessor: Subprocessor adapter.
            :type subprocessor: <ISubProcessor>
            :exceptions:
                | ATSValueError: Subprocessor must be provided.
        '''
        if subprocessor is None:
            raise ATSValueError("subprocessor must be provided.")

        self._subprocessor: ISubProcessor = subprocessor

    @override
    def execute(self, params: dict[str, Any]) -> dict[str, Any]:
        '''
            Executes a tool using the subprocessor adapter.

            :param params: Parameters for tool execution.
            :type params: <dict[str, Any]>
            :return: The result of the tool execution.
            :rtype: <dict[str, Any]>
            :exceptions:
                | ATSValueError: Params dict must be provided.
        '''
        if not params:
            raise ATSValueError("params dict must be provided.")

        tool: Tool = Tool.from_params(params=params)

        if tool:
            return self._subprocessor.run(tool.params)

        return {}

    @override
    def is_initialized(self) -> bool:
        '''
            Checks if the service is initialized.

            :return: True if the service is initialized, False otherwise.
            :rtype: <bool>
            :exceptions: None.
        '''
        return self._subprocessor is not None

    @override
    def __str__(self) -> str:
        '''
            Returns the Service as string representation.

            :return: The Service as string representation.
            :rtype: <str>
            :exceptions: None.
        '''
        return format_instance_to_string(self)
