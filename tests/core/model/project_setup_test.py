# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
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
    Defines unit tests for ProjectSetup domain model.
'''

from __future__ import annotations

from dataclasses import FrozenInstanceError
from unittest import TestCase, main

from gen_py_tool.core.model.project_setup import ProjectSetup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestProjectSetup(TestCase):
    '''
        Defines unit tests for ProjectSetup domain model.

        It defines:

            :methods:
                | test_create_project_setup - Verifies ProjectSetup attributes.
                | test_immutability - Verifies ProjectSetup is frozen and immutable.
    '''

    def test_create_project_setup(self) -> None:
        '''
            Verifies ProjectSetup attributes.

            :exceptions: None.
        '''
        setup: ProjectSetup = ProjectSetup(name='my_tool', output='./demo')
        self.assertEqual(setup.name, 'my_tool')
        self.assertEqual(setup.output, './demo')

    def test_immutability(self) -> None:
        '''
            Verifies ProjectSetup is frozen and immutable.

            :exceptions: None.
        '''
        setup: ProjectSetup = ProjectSetup(name='my_tool', output='./demo')
        with self.assertRaises(FrozenInstanceError):
            setattr(setup, 'name', 'other')


if __name__ == '__main__':
    main()

