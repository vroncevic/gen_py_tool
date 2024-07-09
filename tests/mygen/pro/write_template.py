# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
Copyright
    Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    mygen is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    mygen is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for write operation of template content.
'''

import sys
from typing import List, Dict
from os import getcwd, chmod
from string import Template
from datetime import date

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/mygen'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/mygen/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for writing source and build modules.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - Writes a templates with parameters.
    '''

    _GEN_VERBOSE: str = 'MYGEN::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        templates: Dict[str, str],
        pro_name: Optional[str],
        verbose: bool = False
    ) -> bool:
        '''
            Writes a templates with parameters.

            :param templates: Templates with params
            :type templates: Dict[str, str]
            :param pro_name: Project name | None
            :type pro_name: <Optional[str]>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: Optional[str] = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('dict:templates', templates), ('str:pro_name', pro_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(templates):
            raise ATSValueError('missing templates')
        status: bool = False
        for module, content in templates.items():
            module_path: str = f'{getcwd()}/{module}'
            package: Dict[str, str] = {
                'PRO_NAME': f'{pro_name}',
                'YEAR': f'{str(date.today().year)}'
            }
            template: Template = Template(content)
            if template:
                with open(module_path, 'w', encoding='utf-8') as module_file:
                    module_file.write(template.substitute(package))
                    chmod(module_path, 0o666)
                    self.check_path(module_path, verbose=verbose)
                    self.check_mode('w', verbose=verbose)
                    self.check_format(module_path, 'py', verbose=verbose)
                    if self.is_file_ok():
                        status = True
        return status
