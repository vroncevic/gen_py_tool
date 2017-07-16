# encoding: utf-8

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class FormatName(object):
    """
    Define class FormatName with attribute(s) and method(s).
    Generate and format file name.
    It defines:
        attribute:
            MAIN - 0 Main module
            PROCESS - 1  Process module
            CONF - 2 Configuration module
            __FORMAT_NAME_PY - Python filename extension
            __FORMAT_NAME_CFG - Configuration filename extension
        method:
            format_name - Formatting name for tool
            editor_config - Generating content of github configuration editor
    """

    MAIN, PROCESS, CONF = range(3)
    __FORMAT_NAME_PY = '.py'
    __FORMAT_NAME_CFG = '.cfg'

    @classmethod
    def format_name(cls, tool_name, module_type):
        """
        Formatting name for tool.
        :param tool_name: Tool name (translate to lower case)
        :type: str
        :param module_type: Type of tool (Main/Process/Configuration)
        :type: str
        :return: File name with extension
        :rtype: str
        """
        tool_name_lower = tool_name.lower()
        if module_type == FormatName.MAIN:
            tool_name_final = "{0}_run{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_PY
            )
        elif module_type == FormatName.CONF:
            tool_name_final = "{0}{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_CFG
            )
        else:
            tool_name_final = "{0}{1}".format(
                tool_name_lower, FormatName.__FORMAT_NAME_PY
            )
        return tool_name_final

    @classmethod
    def editor_config(cls, file_format):
        """
        Generating content of github configuration editor.
        :param file_format: File extension
        :type file_format: str
        :return: Content for github editor
        :rtype: str
        """
        editor_config = "[ **.{0}]\nindent_style = tab\ntab_width = 4".format(
            file_format
        )
        return editor_config
