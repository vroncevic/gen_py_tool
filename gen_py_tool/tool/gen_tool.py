# -*- coding: UTF-8 -*-

"""
 Module
     gen_tool.py
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
     Define class GenTool with attribute(s) and method(s).
     Generate python tool by template and parameters.
"""

import sys
from inspect import stack

try:
    from read_template import ReadTemplate
    from write_template import WriteTemplate
    from tool_structure import ToolStructure
    from format_name import FormatName
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenTool(object):
    """
        Define class GenTool with attribute(s) and method(s).
        Generate python tool by template and parameters.
        It defines:

            :attributes:
                | __slots__ - Setting class slots
                | VERBOSE - Console text indicator for current process-phase
                | __STATUS - Status dictionary
                | __reader - Reader API
                | __writer - Writer API
            :methods:
                | __init__ - Initial constructor
                | get_reader - Getter for reader object
                | get_writer - Getter for writer object
                | gen_module - Generate python tool
    """

    __slots__ = ('VERBOSE', '__STATUS', '__reader', '__writer')
    VERBOSE = 'GEN_PY_TOOL::TOOL::GEN_TOOL'
    __STATUS = {
        FormatName.MAIN: 'main',
        FormatName.PROCESS: 'process',
        FormatName.CONF: 'configuration'
    }

    def __init__(self, verbose=False):
        """
            Initial constructor.

            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenTool.VERBOSE, verbose, 'Initial generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def get_reader(self):
        """
            Getter for reader object.

            :return: Read template object
            :rtype: <ReadTemplate>
            :exceptions: None
        """
        return self.__reader

    def get_writer(self):
        """
            Getter for writer object.

            :return: Write template object
            :rtype: <WriteTemplate>
            :exceptions: None
        """
        return self.__writer

    def gen_tool(self, tool_name, verbose=False):
        """
            Generate python tool.

            :param tool_name: Parameter tool name
            :type tool_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Boolean status True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        status, generated_structure, func = False, False, stack()[0][3]
        tool_name_txt = 'Argument: expected tool_name <str> object'
        tool_name_msg = "{0} {1} {2}".format('def', func, tool_name_txt)
        if tool_name is None or not tool_name:
            raise ATSBadCallError(tool_name_msg)
        if not isinstance(tool_name, str):
            raise ATSTypeError(tool_name_msg)
        generated_structure = ToolStructure.gen_structure(
            tool_name, verbose=verbose
        )
        if generated_structure:
            main = self.__reader.read(FormatName.MAIN, verbose=verbose)
            process = self.__reader.read(FormatName.PROCESS, verbose=verbose)
            conf = self.__reader.read(FormatName.CONF, verbose=verbose)
            template_read_status = {
                GenTool.__STATUS[FormatName.MAIN]: main,
                GenTool.__STATUS[FormatName.PROCESS]: process,
                GenTool.__STATUS[FormatName.CONF]: conf
            }
            template_reads = template_read_status.values()
            loaded_templates = all(r_status for r_status in template_reads)
            if loaded_templates:
                main = self.__writer.write(
                    template_read_status[GenTool.__STATUS[FormatName.MAIN]],
                    tool_name, FormatName.MAIN, verbose=verbose
                )
                process = self.__writer.write(
                    template_read_status[GenTool.__STATUS[FormatName.PROCESS]],
                    tool_name, FormatName.PROCESS, verbose=verbose
                )
                conf = self.__writer.write(
                    template_read_status[GenTool.__STATUS[FormatName.CONF]],
                    tool_name, FormatName.CONF, verbose=verbose
                )
                template_write_status = {
                    GenTool.__STATUS[FormatName.MAIN]: main,
                    GenTool.__STATUS[FormatName.PROCESS]: process,
                    GenTool.__STATUS[FormatName.CONF]: conf
                }
                template_writes = template_write_status.values()
                status = all(w_status for w_status in template_writes)
        return True if status else False
