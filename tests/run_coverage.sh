#!/bin/bash
#
# @brief   gen_py_tool
# @version v1.0.1
# @date    Sun Jun  9 07:07:23 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 -m coverage run -m --source=../gen_py_tool unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html

