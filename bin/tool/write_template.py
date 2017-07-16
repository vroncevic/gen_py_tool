# encoding: utf-8

from os import getcwd, chmod
from os.path import exists
from datetime import date
from string import Template
from tool.format_name import FormatName

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplate(object):
    """
    Define class WriteTemplate with attribute(s) and method(s).
    Write a template content with parameters to a file.
    It defines:
        attribute:
            __CHMOD - Change mode code
            __EDITOR_CONFIG - GitHub online editor configuration
            __EDITOR_CONFIG_PY - Python extension name
            __EDITOR_CONFIG_CFG - Configuration extension name
            __CLASS - Class key for template
            __FILE - File key for template
            __DATE - Date key for template
        method:
            __init__ - Initial constructor
            write - Write a template content with parameters to a file
    """

    __CHMOD = 0o666
    __EDITOR_CONFIG = '.editorconfig'
    __EDITOR_CONFIG_PY = 'py'
    __EDITOR_CONFIG_CFG = 'cfg'
    __CLASS = 'TOOL_PROCESS_CLASS'
    __FILE = 'TOOL_PROCESS_FILE'
    __DATE = 'DATE'

    def __init__(self):
        """
        Initial constructor.
        """
        pass

    def write(self, module_content, module_name, module_type):
        """
        Write a template content with parameters to a file.
        :param module_content: Template content
        :type: str
        :param module_name: File name
        :type: str
        :param module_type: Type of module
        :type: str
        :return: Boolean status
        :rtype: bool
        """
        status = False
        current_dir = getcwd()
        module_name_lower = module_name.lower()
        if module_type == FormatName.MAIN or module_type == FormatName.PROCESS:
            prefix_dir = "{0}/{1}/bin".format(current_dir, module_name_lower)
            github_editor = FormatName.editor_config(
                WriteTemplate.__EDITOR_CONFIG_PY
            )
        else:
            prefix_dir = "{0}/{1}/conf".format(current_dir, module_name_lower)
            github_editor = FormatName.editor_config(
                WriteTemplate.__EDITOR_CONFIG_CFG
            )
        module_formatted_name = FormatName.format_name(module_name, module_type)
        module_file_name = "{0}/{1}".format(prefix_dir, module_formatted_name)
        today = date.today()
        module = {
            WriteTemplate.__CLASS: "{0}".format(module_name),
            WriteTemplate.__FILE: "{0}".format(module_name_lower),
            WriteTemplate.__DATE: "{0}".format(today)
        }
        github_editor_file_path = "{0}/{1}".format(
            prefix_dir, WriteTemplate.__EDITOR_CONFIG
        )
        try:
            template = Template(module_content)
            module_file = open(module_file_name, 'w')
            module_content = template.substitute(module)
            module_file.write(module_content)
            github_editor_file_exists = exists(github_editor_file_path)
            if not github_editor_file_exists:
                github_file_editor = open(github_editor_file_path, 'w')
                github_file_editor.write(github_editor)
                github_file_editor.close()
                chmod(path=github_editor_file_path, mode=WriteTemplate.__CHMOD)
        except (IOError, KeyError) as e:
            msg = "I/O error({0}): {1}".format(e.errno, e.strerror)
            print(msg)
        else:
            module_file.close()
            chmod(path=module_file_name, mode=WriteTemplate.__CHMOD)
            status = True
        return True if status else False
