#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Define setup for gen_py_tool package.
'''

from sys import argv, version_info, prefix, exit
from os.path import abspath, dirname, join, exists
from site import getusersitepackages
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.2.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

def install_directory():
    '''
        Return the installation directory, or None.

        :return: Path (success) | None.
        :rtype: <str> | <NoneType>
        :exceptions: None
    '''
    py_version = '{0}.{1}'.format(version_info[0], version_info[1])
    if '--github' in argv:
        index = argv.index('--github')
        argv.pop(index)
        paths = (
            '{0}/lib/python{1}/dist-packages/'.format(prefix, py_version),
            '{0}/lib/python{1}/site-packages/'.format(prefix, py_version)
        )
    else:
        paths = (s for s in (
            '{0}/local/lib/python{1}/dist-packages/'.format(
                prefix, py_version
            ),
            '{0}/local/lib/python{1}/site-packages/'.format(
                prefix, py_version
            )
        ))
    for path in paths:
        print('[setup] check path {0}'.format(path))
        if exists(path):
            print('[setup] using path {0}'.format(path))
            return path
    print('[setup] no installation path found, check {0}\n'.format(prefix))
    return None

INSTALL_DIR = install_directory()

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

CONF = 'gen_py_tool/conf/'
TEMPLATE_TOOL = '{0}{1}'.format(CONF, 'template/tool/')
TEMPLATE_GEN = '{0}{1}'.format(CONF, 'template/generator/')
LOG = 'gen_py_tool/log/'

setup(
    name='gen_py_tool',
    version='1.2.0',
    description='Generating python tool',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool/',
    license='GPL 2020 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Python, Tool',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_py_tool', 'gen_py_tool.pro'],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_py_tool/run/gen_py_tool_run.py']),
        (
            '{0}{1}'.format(INSTALL_DIR, CONF),
            ['gen_py_tool/conf/gen_py_tool.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, CONF),
            ['gen_py_tool/conf/gen_py_tool_util.cfg']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, CONF),
            ['gen_py_tool/conf/project.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, CONF),
            ['gen_py_tool/conf/schema_tool.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, CONF),
            ['gen_py_tool/conf/schema_generator.yaml']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_TOOL),
            ['gen_py_tool/conf/template/editorconfig.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_TOOL),
            ['gen_py_tool/conf/template/run_module.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_TOOL),
            ['gen_py_tool/conf/template/tool_configuration.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_TOOL),
            ['gen_py_tool/conf/template/tool_configuration_util.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_TOOL),
            ['gen_py_tool/conf/template/tool_process_class.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/editorconfig.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/generator_configuration.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/generator_configuration_util.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/generator_process_class.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/generator_read_template.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/generator_write_template.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, TEMPLATE_GEN),
            ['gen_py_tool/conf/template/run_module.template']
        ),
        (
            '{0}{1}'.format(INSTALL_DIR, LOG),
            ['gen_py_tool/log/gen_py_tool.log']
        )
    ]
)
