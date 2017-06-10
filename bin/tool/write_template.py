# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

from os import getcwd, chmod
from os.path import exists
from datetime import date
from string import Template
from tool.format_name import FormatName

class WriteTemplate(object):
	"""
	Define class WriteTemplate with attribute(s) and method(s).
	Write a template content with parameters to a file.
	It defines:
		attribute:
			None
		method:
			__init__ - Initial constructor
			write - Write a template content with parameters to a file
	"""

	def __init__(self):
		pass

	def write(self, module_content, module_name, module_type):
		"""
		:param module_content: Template content
		:type: str
		:param module_name: File name
		:type: str
		:param module_type: Type of module
		:type: str
		:return: Boolean status
		:rtype: bool
		"""
		current_dir = getcwd()
		if module_type == FormatName.MAIN or module_type == FormatName.PROCESS:
			prefix_dir = "{0}/{1}/bin".format(current_dir, module_name.lower())
			github_editor = FormatName.editor_config("py")
		else:
			prefix_dir = "{0}/{1}/conf".format(current_dir, module_name.lower())
			github_editor = FormatName.editor_config("cfg")
		module_file_name = "{0}/{1}".format(
			prefix_dir, FormatName.format_name(module_name, module_type)
		)
		module = {
			"TOOL_PROCESS_CLASS" : "{0}".format(module_name),
			"TOOL_PROCESS_FILE": "{0}".format(module_name.lower()),
			"DATE" : "{0}".format(date.today())
		}
		ed_file = "{0}/{1}".format(prefix_dir, ".editorconfig")
		try:
			template = Template(module_content)
			module_file = open(module_file_name, "w")
			module_file.write(template.substitute(module))
			if not exists(ed_file):
				ed_fh = open(ed_file, "w")
				ed_fh.write(github_editor)
				ed_fh.close()
				chmod(path=ed_file, mode=0o666)
		except (IOError, KeyError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))
		else:
			module_file.close()
			chmod(path=module_file_name, mode=0o666)
			return True
		return False
