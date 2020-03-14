# Generate Python Tool

gen_py_tool is toolset for generation Py Tool.

Developed in python code: 100%.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

![Python package](https://github.com/vroncevic/gen_py_tool/workflows/Python%20package/badge.svg)
 [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/issues)
 [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/graphs/contributors)

### INSTALLATION
Navigate to release [page](https://github.com/vroncevic/gen_py_tool/releases) download and extract release archive.

To install this set of modules type the following:

```
tar xvzf gen_py_tool-x.y.z.tar.gz
cd gen_py_tool-x.y.z/python-tool
cp -R ~/bin/   /root/scripts/gen_py_tool/
cp -R ~/conf/  /root/scripts/gen_py_tool/
cp -R ~/log/   /root/scripts/gen_py_tool/
```

### DEPENDENCIES

This module requires these other modules and libraries:


* ats_utilities https://vroncevic.github.io/ats_utilities

### GENERATION FLOW OF PY TOOL

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/python-tool-docs/gen_py_tool_flow.png)

### TOOL STRUCTURE

gen_py_tool is based on Template mechanism:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/python-tool-docs/gen_py_tool.png)

Generator structure:

```
.
├── bin
│   ├── gen_py_tool.py
│   ├── gen_py_tool_run.py
│   └── tool
│       ├── format_name.py
│       ├── gen_tool.py
│       ├── __init__.py
│       ├── read_template.py
│       ├── tool_structure.py
│       └── write_template.py
├── conf
│   ├── gen_py_tool.cfg
│   ├── gen_py_tool_util.cfg
│   └── template
│       ├── editorconfig.template
│       ├── main_module.template
│       ├── tool_configuration.template
│       └── tool_process_class.template
└── log
    └── gen_py_tool.log

```

### COPYRIGHT AND LICENCE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Copyright (C) 2018 by https://vroncevic.github.io/gen_py_tool

This tool is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.4.2 or,
at your option, any later version of Python 3 you may have available.

:sparkles:

