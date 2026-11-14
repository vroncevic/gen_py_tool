# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Engine orchestrating the initialization and execution of gen_py_tool.
'''

from __future__ import annotations

from collections.abc import Mapping
from logging import ERROR, INFO
from sys import stdout

from ats_utilities.base.engine import Base
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger

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


class GenPyTool(Base):
    '''
        Engine orchestrating the initialization and execution of gen_py_tool.

        It defines:

            :attributes:
                | _is_initialized - Flag indicating whether the engine is initialized.
                | _logger - Logger for operational messages during initialization and execution.
                | _cli - Inbound adapter for the command line interface.
            :methods:
                | __init__ - Initializes the GenPyTool engine with validated bundle.
                | process - Processes the gen_py_tool commands.
    '''

    _is_initialized: bool
    _logger: ILogger
    _cli: ICLI

    def __init__(self, bundle: GenPyToolBundle) -> None:
        '''
            Initializes the GenPyTool engine with validated bundle.

            :param bundle: GenPyTool bundle containing adapters and services.
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            GenPyToolBundleValidator.validate(bundle)
            super().__init__(bundle.base)

            self._is_initialized = False
            self._cli = bundle.cli
            self._is_initialized = all(
                component.is_initialized() for component in (
                    bundle.base.option_manager,
                    bundle.service,
                    bundle.subprocessor,
                    self._cli
                ) if component
            )

            self._logger = self.get_context().logger
            self._logger.write_log(INFO, '✅ gen_py_tool: engine initialized successfully!')

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ gen_py_tool: {exc}!\n')

        except Exception as exc:
            stdout.write(f'❌ gen_py_tool unexpected exception: {exc}!\n')

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes the gen_py_tool commands.

            :param verbose: Enable verbose output.
            :return: True if successful, False otherwise.
            :exceptions: None.
        '''
        _ = verbose

        try:
            if self.is_initialized():
                self._logger.write_log(INFO, '🔥 Starting execution command...')
                result: Mapping[str, object] = self._cli.run()
                self._logger.write_log(INFO, '✅ Execution finished!')

                if result.get('returncode') != 0:
                    self._logger.write_log(ERROR, f'❌ gen_py_tool: {result.get("stderr") or "failed!"}')
                    return False

                self._logger.write_log(INFO, '✅ gen_py_tool: done!')
                self._logger.write_log(INFO, '✅ gen_py_tool: exiting successfully!')
                return True

            stdout.write('❌ gen_py_tool: engine not initialized!\n')
            return False

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ gen_py_tool: {exc}!\n')
            return False

        except Exception as exc:
            stdout.write(f'❌ gen_py_tool unexpected exception: {exc}!\n')
            return False
