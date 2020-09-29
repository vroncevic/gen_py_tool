#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
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
"""

from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

setup(
    name='gen_py_tool',
    version='1.0.0',
    description='Generating python tool',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_py_tool/',
    license='GPL 2020 Free software to use and distributed it.',
    long_description='Generating python tool in Unix/Linux OS.',
    keywords='Unix, Linux, Python, Tool',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
    ],
    packages=[
        'gen_py_tool',
        'gen_py_tool.tool',
    ],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_py_tool/run/gen_py_tool_run.py']),
        (
             '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/',
             ['gen_py_tool/conf/gen_py_tool.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/',
            ['gen_py_tool/conf/gen_py_tool_util.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/template/',
            ['gen_py_tool/conf/template/editorconfig.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/template/',
            ['gen_py_tool/conf/template/main_module.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/template/',
            ['gen_py_tool/conf/template/tool_configuration.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/conf/template/',
            ['gen_py_tool/conf/template/tool_process_class.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_py_tool/log/',
            ['gen_py_tool/log/gen_py_tool.log']
        )
    ]
)
