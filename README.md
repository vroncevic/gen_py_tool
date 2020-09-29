# Generate Python Tool

**gen_py_tool** is toolset for generation of Python tool.

Developed in python code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_py_tool/workflows/Python%20package%20gen_py_tool/badge.svg?branch=master)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Generation flow of py tool](#generation-flow-of-py-tool)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Navigate to release **[release page](https://github.com/vroncevic/gen_py_tool/releases)** download and extract release archive.
To install modules, locate and run setup.py, type the following:

```
tar xvzf gen_py_tool-x.y.z.tar.gz
cd gen_py_tool-x.y.z/python-tool
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_egg_info
python setup.py install_data
```

### Dependencies

These modules requires other modules and libraries (Python 2.x/3.x):
* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### Generation flow of py tool

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/python-tool-docs/gen_py_tool_flow.png)

### Tool structure

gen_py_tool is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/python-tool-docs/gen_py_tool.png)

Generator structure:

```
 gen_py_tool
 ├── conf/
 │   ├── gen_py_tool.cfg
 │   ├── gen_py_tool_util.cfg
 │   └── template/
 │       ├── editorconfig.template
 │       ├── main_module.template
 │       ├── tool_configuration.template
 │       └── tool_process_class.template
 ├── __init__.py
 ├── log/
 │   └── gen_py_tool.log
 ├── run/
 │   └── gen_py_tool_run.py
 └── tool/
     ├── format_name.py
     ├── gen_tool.py
     ├── __init__.py
     ├── read_template.py
     ├── tool_structure.py
     └── write_template.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_py_tool/badge/?version=latest)](https://gen_py_tool.readthedocs.io/projects/gen_py_tool/en/latest/?badge=latest)

More documentation and info at:
* [gen_py_tool.readthedocs.io](https://gen_py_tool.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 by [vroncevic.github.io/gen_py_tool](https://vroncevic.github.io/gen_py_tool/)

**gen_py_tool** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

