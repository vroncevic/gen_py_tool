#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
import os
from typing import List, Optional
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_py_tool'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR: str = 'gen_py_tool/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: Optional[str] = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS


def find_package_data(package_name: str) -> list[str]:
    '''
        Finds all files in package to include in package_data.

        :param package_name: Package folder name.
        :type package_name: <str>
        :return: List of package files relative to the package folder.
        :rtype: <list[str]>
        :exceptions: None.
    '''
    package_data = []
    for root, dirs, files in os.walk(package_name):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for file in files:
            if file.endswith('.pyc') or file == '.editorconfig':
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, package_name)
            package_data.append(rel_path)
    return package_data


setup(
    name='gen_py_tool',
    version='1.4.0',
    description='Python package for generation of python tool/generator',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='setup, python, install, tool, generator',
    platforms='any',
    classifiers=PYP_CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['ats-utilities'],
    package_data={
        'gen_py_tool': find_package_data('gen_py_tool')
    }
)
