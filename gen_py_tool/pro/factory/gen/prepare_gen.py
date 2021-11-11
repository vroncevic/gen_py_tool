# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class PrepareGen with attribute(s) and method(s).
     Created API for preparing project schema for generator.
'''

import sys

try:
    from gen_py_tool.pro.factory.collectiner.gen import ProCollectiner
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_py_tool'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class PrepareGen(ProCollectiner):
    '''
        Defined class PrepareGen with attribute(s) and method(s).
        Created API for preparing project schema for generator.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | export - export formatted project schema.
                | __str__ - dunder method for PrepareGen.
    '''

    GEN_VERBOSE = 'GEN_PY_TOOL::PRO::FACTORY::GEN::PREPARE_GEN'

    def __init__(self, pro_property, template, schema, verbose=False):
        '''
            Initial constructor.

            :param pro_property: project property.
            :type pro_property: <dict>
            :param template: project tool/generator template.
            :type template: <dict>
            :param schema: project tool/generator schema.
            :type schema: <dict>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:pro_property', pro_property),
            ('dict:template', template),
            ('dict:schema', schema)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        ProCollectiner.__init__(self)
        self.pro_name = pro_property['name']
        self.pro_type = pro_property['type']
        self.template = template
        self.schema = schema
        verbose_message(
            PrepareGen.GEN_VERBOSE, verbose, 'init prepare generator'
        )

    def export(self, verbose=False):
        '''
            Export generator project setup.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: schema content, boolean status (True) | None, False.
            :rtype: <dict>, <bool> | <NoneType>, <bool>
            :exceptions: None
        '''
        status = False
        self.update_gen_name()
        self.update_gen_class()
        self.update_gen_run()
        self.update_gen_pro_class()
        self.update_gen_conf()
        self.update_gen_log()
        if bool(self.schema):
            status = True
        else:
            error_message(
                PrepareGen.GEN_VERBOSE, 'schema object is not ok'
            )
        verbose_message(PrepareGen.GEN_VERBOSE, verbose, self.schema)
        return self.schema, status

    def __str__(self):
        '''
            Dunder method for PrepareGen.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, ProCollectiner.__str__(self)
        )
