# encoding: utf-8

from os import mkdir, getcwd
from os.path import isdir

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ToolStructure(object):
    """
    Define class ToolStructure with attribute(s) and method(s).
    Generating tool directory structure.
    It defines:
        attribute:
            BIN - 0 Bin directory
            CFG - 1 Configuration directory
            LOG - 2 Logging directory
            __TOOL_SUB_STRUCTURE - Dictionary structure
        method:
            gen_structure - Generating tool directory structure
    """

    __BIN, __CFG, __LOG = range(3)

    __TOOL_SUB_STRUCTURE = {
        __BIN: '/bin/',
        __CFG: '/conf/',
        __LOG: '/log/'
    }

    @classmethod
    def gen_structure(cls, project_name):
        """
        Generating tool directory structure.
        :param project_name: Project root directory name
        :return: Boolean status (structure generated)
        :rtype: bool
        """
        current_dir = getcwd()
        project_name_lower = project_name.lower()
        root_dir = "{0}/{1}".format(current_dir, project_name_lower)
        statuses = []
        mkdir(root_dir)
        check_root_dir = isdir(root_dir)
        statuses.append(check_root_dir)
        bin_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__BIN]
        )
        mkdir(bin_dir)
        check_bin_dir = isdir(bin_dir)
        statuses.append(check_bin_dir)
        conf_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__CFG]
        )
        mkdir(conf_dir)
        check_conf_dir = isdir(conf_dir)
        statuses.append(check_conf_dir)
        log_dir = "{0}{1}".format(
            root_dir, ToolStructure.__TOOL_SUB_STRUCTURE[ToolStructure.__LOG]
        )
        mkdir(log_dir)
        check_log_dir = isdir(log_dir)
        statuses.append(check_log_dir)
        return all(status for status in statuses)
