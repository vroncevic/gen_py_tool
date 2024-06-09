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
from typing import List
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2017 - 2024, https://vroncevic.github.io/gen_py_tool'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.3.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

TOOL_DIR: str = 'gen_py_tool/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
BUILD: str = 'conf/template/build'
SRC: str = 'conf/template/src'
THIS_DIR: str = abspath(dirname(__file__))
long_description: str | None = None
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
    version='1.3.3',
    description='Python package for generation of python tool',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool',
    license='GPL 2021 - 2024 Free software to use and distributed it.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setup, python, install, tool',
    platforms='any',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'gen_py_tool',
        'gen_py_tool.pro',
        'gen_py_tool.pro.config',
        'gen_py_tool.pro.element',
        'gen_py_tool.pro.factory',
        'gen_py_tool.pro.template'
    ],
    install_requires=['ats-utilities'],
    package_data={
        'gen_py_tool': [
            f'{CONF}/gen_py_tool.logo',
            f'{CONF}/gen_py_tool.cfg',
            f'{CONF}/gen_py_tool_util.cfg',
            f'{CONF}/project.yaml',
            f'{CONF}/element/substitute_generator.yaml',
            f'{CONF}/element/substitute_tool.yaml',
            f'{CONF}/schema/schema_tool.yaml',
            f'{CONF}/schema/schema_generator.yaml',
            f'{TEMPLATE}/template_generator.yaml',
            f'{TEMPLATE}/template_tool.yaml',
            f'{TEMPLATE}/tool/editorconfig.template',
            f'{TEMPLATE}/tool/run_tool.template',
            f'{TEMPLATE}/tool/tool_configuration.template',
            f'{TEMPLATE}/tool/tool_configuration_util.template',
            f'{TEMPLATE}/tool/tool_name_class.template',
            f'{TEMPLATE}/generator/editorconfig.template',
            f'{TEMPLATE}/generator/generator_configuration.template',
            f'{TEMPLATE}/generator/generator_configuration_util.template',
            f'{TEMPLATE}/generator/generator_io_class.template',
            f'{TEMPLATE}/generator/generator_process_class.template',
            f'{TEMPLATE}/generator/generator_read_template.template',
            f'{TEMPLATE}/generator/generator_test.template',
            f'{TEMPLATE}/generator/generator_write_template.template',
            f'{TEMPLATE}/generator/run_generator.template',
            f'{LOG}/gen_py_tool.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_py_tool_run.py'
        ]
    )]
)
