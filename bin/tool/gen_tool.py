# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from tool.read_template import ReadTemplate
from tool.write_template import WriteTemplate
from tool.tool_structure import ToolStructure
from tool.format_name import FormatName

class GenTool(ReadTemplate, WriteTemplate):
	"""
	Define class GenTool with attribute(s) and method(s).
	Generate python tool by template and parameters.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			gen_module - Generate file python tool
	"""

	def __init__(self):
		ReadTemplate.__init__(self)
		WriteTemplate.__init__(self)

	def gen_tool(self, tool_name):
		"""
		:param tool_name: Parameter tool name
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		status = False
		if ToolStructure.gen_structure(tool_name):
			r_statuses = {
				"main" : self.read(FormatName.MAIN),
				"process" : self.read(FormatName.PROCESS),
				"configuration" : self.read(FormatName.CONF)
			}
			if all(bool(content) for content in r_statuses.values()):
				w_statuses = {
					"main" : self.write(
						r_statuses["main"], tool_name, FormatName.MAIN
					),
					"process" : self.write(
						r_statuses["process"], tool_name, FormatName.PROCESS
					),
					"configuration" : self.write(
						r_statuses["configuration"], tool_name, FormatName.CONF
					)
				}
				status = all(w_status for w_status in w_statuses.values())
		return status
