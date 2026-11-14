#!/bin/bash
#
# @brief   gen_py_tool
# @version 1.4.2
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_py_tool
pylint gen_py_tool > gen_py_tool.report
echo "Done"
