# -*- coding: UTF-8 -*-
# gen_py_tool.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_py_tool is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_py_tool is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from os import getcwd
from os.path import exists
from datetime import datetime

try:
    from pathlib import Path

    from tool.gen_tool import GenTool
    from ats_utilities.cfg_base import CfgBase
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenPyTool(CfgBase):
    """
        Define class GenPyModule with attribute(s) and method(s).
        Load a settings, create a CL interface and run operation(s).
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __CONFIG - Configuration file path
                __OPS - Tool options (list)
            method:
                __init__ - Initial constructor
                process - Process and run tool option(s)
    """

    __slots__ = ('VERBOSE', '__CONFIG', '__OPS')
    VERBOSE = 'GEN_PY_TOOL'
    __CONFIG = '/../conf/gen_py_tool.cfg'
    __OPS = ['-g', '--gen', '-h', '--version']

    def __init__(self, verbose=False):
        """
            Initial constructor.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenPyTool.VERBOSE, verbose, 'Initial configuration')
        module_dir = Path(__file__).resolve().parent
        base_config_file = "{0}{1}".format(module_dir, GenPyTool.__CONFIG)
        CfgBase.__init__(self, base_config_file, verbose=verbose)
        if self.tool_status:
            self.add_new_option(
                GenPyTool.__OPS[0], GenPyTool.__OPS[1], dest='gen',
                help='generate python tool'
            )

    def process(self, verbose=False):
        """
            Process and run operation.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: None
        """
        status = False
        if self.tool_status:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                option = sys.argv[1]
                if option not in GenPyTool.__OPS:
                    sys.argv = []
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            opts, args = self.parse_args(sys.argv)
            num_of_args, current_dir = len(args), getcwd()
            tool_path = "{0}/{1}".format(current_dir, opts.gen)
            tool_exists = Path(tool_path).exists()
            if num_of_args == 1 and opts.gen and not tool_exists:
                generator, gen_status = GenTool(verbose=verbose), False
                message = "{0} {1} [{2}]".format(
                    "[{0}]".format(self.name),
                    'Generating python tool', opts.gen
                )
                print(message)
                gen_status = generator.gen_tool("{0}".format(opts.gen))
                if gen_status:
                    success_message(self.name, 'Done\n')
                    status = True
                else:
                    error_message(self.name, 'Failed to generate tool')
            else:
                error_message(self.name, 'Tool already exist !')
        else:
            error_message('gen_py_tool', 'Tool is not operational')
        return True if status else False

