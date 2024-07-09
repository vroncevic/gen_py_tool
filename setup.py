#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
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
    Defines setup for tool gen_py_tool.
'''

from __future__ import print_function
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_py_tool'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.3.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

TOOL_DIR: str = 'gen_py_tool/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
LICENSE_PREFIX: str = 'License :: OSI Approved ::'
LICENSES: List[str] = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES: List[str] = [
    f'{LICENSE_PREFIX} {LICENSE}' for LICENSE in LICENSES
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_py_tool',
    version='1.3.6',
    description='Python package for generation of python tool/generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool',
    license='GPL 2017 - 2024 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setup, python, install, tool, generator',
    platforms='any',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_py_tool', 'gen_py_tool.pro'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_py_tool': [
            'py.typed',
            f'{CONF}/gen_py_tool.logo',
            f'{CONF}/gen_py_tool.cfg',
            f'{CONF}/gen_py_tool_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/tool/editorconfig.template',
            f'{TEMPLATE}/tool/tool_class.template',
            f'{TEMPLATE}/tool/tool_config_util.template',
            f'{TEMPLATE}/tool/tool_config.template',
            f'{TEMPLATE}/tool/tool_log.template',
            f'{TEMPLATE}/tool/tool_logo.template',
            f'{TEMPLATE}/tool/tool_run.template',
            f'{TEMPLATE}/gen/editorconfig.template',
            f'{TEMPLATE}/gen/gen_class.template',
            f'{TEMPLATE}/gen/gen_config_util.template',
            f'{TEMPLATE}/gen/gen_config.template',
            f'{TEMPLATE}/gen/gen_log.template',
            f'{TEMPLATE}/gen/gen_logo.template',
            f'{TEMPLATE}/gen/gen_pro_class.template',
            f'{TEMPLATE}/gen/gen_pro_yaml.template',
            f'{TEMPLATE}/gen/gen_project_yaml.template',
            f'{TEMPLATE}/gen/gen_read_template.template',
            f'{TEMPLATE}/gen/gen_run.template',
            f'{TEMPLATE}/gen/gen_write_template.template',
            f'{TEMPLATE}/gen/test.template',
            f'{LOG}/gen_py_tool.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_py_tool_run.py'
        ]
    )]
)
