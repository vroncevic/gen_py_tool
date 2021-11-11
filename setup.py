#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define setup for tool gen_py_tool.
'''

from __future__ import print_function
import sys
from os.path import abspath, dirname, join, exists
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(sys.version_info[0], sys.version_info[1])
    if '--github' in sys.argv:
        index = sys.argv.index('--github')
        sys.argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(sys.prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(sys.prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                sys.prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                sys.prefix, py_version
            )
        ))
    message = None
    for path in paths:
        message = '[setup] check path {0}'.format(path)
        print(message)
        if exists(path):
            message = '[setup] use path {0}'.format(path)
            print(message)
            return path
    message = '[setup] no installation path found, check {0}\n'.format(
        sys.prefix
    )
    print(message)
    return None

INSTALL_DIR = install_directory()
TOOL_DIR = 'gen_py_tool/'
if not INSTALL_DIR:
    print('[setup] force exit from install process')
    exit(127)
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_py_tool',
    version='1.2.3',
    description='Generating python tool',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool/',
    license='GPL 2017 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Python, Tool, Generator, Template',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'gen_py_tool',
        'gen_py_tool.pro',
        'gen_py_tool.pro.config',
        'gen_py_tool.pro.element',
        'gen_py_tool.pro.factory',
        'gen_py_tool.pro.factory.tool',
        'gen_py_tool.pro.factory.gen',
        'gen_py_tool.pro.factory.collectiner',
        'gen_py_tool.pro.factory.collectiner.gen',
        'gen_py_tool.pro.factory.collectiner.tool',
        'gen_py_tool.pro.factory.extractiner',
        'gen_py_tool.pro.factory.extractiner.gen',
        'gen_py_tool.pro.factory.extractiner.tool',
        'gen_py_tool.pro.schema',
        'gen_py_tool.pro.template'
    ],
    install_requires=['ats-utilities'],
    package_data = {
        'gen_py_tool': [
            'conf/gen_py_tool.cfg',
            'conf/gen_py_tool_util.cfg',
            'conf/project.yaml',
            'conf/element/substitute_generator.yaml',
            'conf/element/substitute_tool.yaml',
            'conf/schema/schema_tool.yaml',
            'conf/schema/schema_generator.yaml',
            'conf/template/template_generator.yaml',
            'conf/template/template_tool.yaml',
            'conf/template/tool/editorconfig.template',
            'conf/template/tool/run_tool.template',
            'conf/template/tool/tool_configuration.template',
            'conf/template/tool/tool_configuration_util.template',
            'conf/template/tool/tool_name_class.template',
            'conf/template/generator/editorconfig.template',
            'conf/template/generator/generator_configuration.template',
            'conf/template/generator/generator_configuration_util.template',
            'conf/template/generator/generator_io_class.template',
            'conf/template/generator/generator_process_class.template',
            'conf/template/generator/generator_read_template.template',
            'conf/template/generator/generator_test.template',
            'conf/template/generator/generator_write_template.template',
            'conf/template/generator/run_generator.template',
            'log/gen_py_tool.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            '{0}{1}'.format(TOOL_DIR, 'run/gen_py_tool_run.py')
        ]
    )]
)
