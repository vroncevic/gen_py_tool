# -*- coding: UTF-8 -*-

'''
Module
    definition_test.py
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
    Defines unit tests for CommandDefinition class.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_py_tool.infrastructure.command.definition import CommandDefinition

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCommandDefinition(TestCase):
    '''
        Defines unit tests for CommandDefinition class.

        It defines:

            :methods:
                | test_properties - Verifies name, help_text, and options properties.
                | test_str - Verifies string representation.
    '''

    def test_properties(self) -> None:
        '''
            Verifies name, help_text, and options properties.

            :exceptions: None.
        '''
        definition: CommandDefinition = CommandDefinition()
        self.assertEqual(definition.name, 'create')
        self.assertNotEqual(definition.help_text, '')
        self.assertEqual(len(definition.options), 2)
        self.assertEqual(definition.options[0].name, '--name')
        self.assertEqual(definition.options[1].name, '--output')

    def test_str(self) -> None:
        '''
            Verifies string representation.

            :exceptions: None.
        '''
        self.assertIsInstance(str(CommandDefinition()), str)


if __name__ == '__main__':
    main()

