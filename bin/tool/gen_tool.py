# encoding: utf-8

from tool.read_template import ReadTemplate
from tool.write_template import WriteTemplate
from tool.tool_structure import ToolStructure
from tool.format_name import FormatName

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenTool(ReadTemplate, WriteTemplate):
    """
    Define class GenTool with attribute(s) and method(s).
    Generate python tool by template and parameters.
    It defines:
        attribute:
            __STATUS - Status dictionary
        method:
            __init__ - Initial constructor
            gen_module - Generate python tool
    """

    __STATUS = {
        FormatName.MAIN: 'main',
        FormatName.PROCESS: 'process',
        FormatName.CONF: 'configuration'
    }

    def __init__(self):
        """
        Setting template reader and writer.
        """
        ReadTemplate.__init__(self)
        WriteTemplate.__init__(self)

    def gen_tool(self, tool_name):
        """
        Generate python tool.
        :param tool_name: Parameter tool name
        :type: str
        :return: Boolean status
        :rtype: bool
        """
        status = False
        generated_structure = ToolStructure.gen_structure(tool_name)
        if generated_structure:
            main = self.read(FormatName.MAIN)
            process = self.read(FormatName.PROCESS)
            conf = self.read(FormatName.CONF)
            template_read_status = {
                GenTool.__STATUS[FormatName.MAIN]: main,
                GenTool.__STATUS[FormatName.PROCESS]: process,
                GenTool.__STATUS[FormatName.CONF]: conf
            }
            loaded_templates = all(
                r_status for r_status in template_read_status.values()
            )
            if loaded_templates:
                main = self.write(
                    template_read_status[GenTool.__STATUS[FormatName.MAIN]],
                    tool_name,
                    FormatName.MAIN
                )
                process = self.write(
                    template_read_status[GenTool.__STATUS[FormatName.PROCESS]],
                    tool_name,
                    FormatName.PROCESS
                )
                conf = self.write(
                    template_read_status[GenTool.__STATUS[FormatName.CONF]],
                    tool_name,
                    FormatName.CONF
                )
                template_write_status = {
                    GenTool.__STATUS[FormatName.MAIN]: main,
                    GenTool.__STATUS[FormatName.PROCESS]: process,
                    GenTool.__STATUS[FormatName.CONF]: conf
                }
                status = all(
                    w_status for w_status in template_write_status.values()
                )
        return True if status else False
