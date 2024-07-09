#!/bin/bash
#
# @brief   gen_py_tool
# @version v1.0.1
# @date    Sun Jun  9 07:07:23 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_py_tool_coverage.xml gen_py_tool_coverage.json .coverage
rm -rf mytool mygen
ats_coverage_run.py -n gen_py_tool -p ../README.md
rm -rf mytool mygen
python3 -m coverage run -m --source=../gen_py_tool unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_py_tool_coverage.xml 
python3 -m coverage json -o gen_py_tool_coverage.json
python3 -m coverage report --format=markdown -m
