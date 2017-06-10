# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class FormatName(object):
	"""
	Define class FormatName with attribute(s) and method(s).
	Generate and format file name.
	It defines:
		attribute:
			MAIN - 0 Main module
			PROCESS - 1  Process module
		method:
			format_name - Formatting name for file tool
	"""

	MAIN, PROCESS, CONF = range(3)

	@classmethod
	def format_name(cls, tool_name, module_type):
		"""
		:param tool_name: Tool name (translate to lower case)
		:type: str
		:param module_type: Type of tool (Main/Process)
		:type: str
		:return: File name with extension
		:rtype: str
		"""
		if module_type == FormatName.MAIN:
			return "{0}_run{1}".format(tool_name.lower(), ".py")
		elif module_type == FormatName.CONF:
			return  "{0}{1}".format(tool_name.lower(), ".cfg")
		return "{0}{1}".format(tool_name.lower(), ".py")

	@classmethod
	def editor_config(cls, file_format):
		"""
		:param file_format: File extension
		:type file_format: str
		:return: Content for github editor
		:rtype: str
		"""
		return "[ **.{0}]\nindent_style = tab\ntab_width = 4".format(
			file_format
		)
