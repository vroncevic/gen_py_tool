# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for writing source and build modules.
'''

import sys
from typing import List, Dict
from datetime import date
from os import getcwd, chmod, mkdir
from os.path import exists
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_py_tool'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.3.4'
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

    _GEN_VERBOSE: str = 'GEN_PY_TOOL::PRO::WRITE_TEMPLATE'

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
        templates: List[Dict[str, str]],
        pro_name: str | None,
        verbose: bool = False
    ) -> bool:
        '''
            Writes a templates with parameters.

            :param templates: Templates with params
            :type templates: <List[Dict[str, str]]>
            :param pro_name: Project name | None
            :type pro_name: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('list:templates', templates), ('str:pro_name', pro_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(templates):
            raise ATSValueError('missing templates')
        all_stat: List[bool] = []
        pro_dir: str = f'{getcwd()}/{pro_name}/'
        conf_dir: str = f'{getcwd()}/{pro_name}/conf/'
        tmp_dir: str = f'{getcwd()}/{pro_name}/conf/template/'
        run_dir: str = f'{getcwd()}/{pro_name}/run/'
        log_dir: str = f'{getcwd()}/{pro_name}/log/'
        gen_dir: str = f'{getcwd()}/{pro_name}/pro/'
        num_of_modules: int = len(templates)
        if not exists(pro_dir):
            mkdir(pro_dir)
            mkdir(gen_dir)
            mkdir(conf_dir)
            mkdir(tmp_dir)
            mkdir(run_dir)
            mkdir(log_dir)
        for template_content in templates:
            module_name: str = list(template_content.keys())[0]
            module_path: str = f'{pro_dir}{module_name}'
            if 'cfg' in module_name:
                module_path = f'{conf_dir}{module_name}'
            if 'run' in module_name:
                module_path = f'{run_dir}{module_name}'
            if 'logo' in module_name:
                module_path = f'{conf_dir}{module_name}'
            if 'log' in module_name and 'logo' not in module_name:
                module_path = f'{log_dir}{module_name}'
            if 'test' in module_name:
                module_path = f'{tmp_dir}{module_name}'
            if 'pro' in module_name:
                module_path = f'{gen_dir}__init__.py'
            if 'project.yaml' in module_name:
                module_path = f'{conf_dir}{module_name}'
            if 'read_template' in module_name:
                module_path = f'{gen_dir}{module_name}'
            if 'write_template' in module_name:
                module_path = f'{gen_dir}{module_name}'
            template: Template = Template(template_content[module_name])
            template_path: Template = Template(module_path)
            module_path = template_path.substitute({'PRO_NAME': f'{pro_name}'})
            if exists(module_path):
                raise FileExistsError(f'{module_path} already exists')
            with open(module_path, 'w', encoding='utf-8') as module_file:
                module_content: str = template.substitute({
                    'PRO_NAME': f'{pro_name}',
                    'PRO_NAME_CLASS': f'{pro_name}'.format().capitalize(),
                    'PRO_NAME_UPPER': f'{pro_name}'.format().upper(),
                    'PRO_NAME_GEN': f'{pro_name}'.format().capitalize() + 'Gen',
                    'PRO_NAME_GEN_UPPER': f'{pro_name}Gen'.format().upper(),
                    'DATE': f'{str(date.today())}',
                    'YEAR': f'{str(date.today().year)}'
                })
                module_file.write(module_content)
                chmod(module_path, 0o666)
                self.check_path(module_path, verbose)
                self.check_mode('w', verbose)
                self.check_format(
                    module_path, module_path.split('.')[1], verbose
                )
                if self.is_file_ok():
                    all_stat.append(True)
                else:
                    all_stat.append(False)
        return all([
            bool(all_stat), all(all_stat), len(all_stat) == num_of_modules
        ])
