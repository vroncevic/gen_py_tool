# Generate Python Tool

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/gen_py_tool_logo.png" width="25%">

**gen_py_tool** is toolset for generation of Python tool.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_py_tool python checker](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python_checker.yml) [![gen_py_tool package checker](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_py_tool.svg)](https://github.com/vroncevic/gen_py_tool/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/debtux.png)

[![gen_py_tool python3 build](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_py_tool** is located at **[pypi.org](https://pypi.org/project/gen_py_tool/)**.

You can install by using pip

```bash
# python3
pip3 install gen_py_tool
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_py_tool/releases/)** download and extract release archive.

To install **gen_py_tool** type the following

```bash
tar xvzf gen_py_tool-x.y.z.tar.gz
cd gen_py_tool-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_py_tool-*-py3-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_py_tool_run.py
ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_py_tool_run.py /usr/local/bin/gen_py_tool_run.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_py_tool/releases)** download and extract release archive.

To install **gen_py_tool** locate and run setup.py with arguments

```bash
tar xvzf gen_py_tool-x.y.z.tar.gz
cd gen_py_tool-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### Dependencies

**gen_py_tool** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### Tool structure

**gen_py_tool** is based on OOP

Generator structure

```bash
    gen_py_tool/
       ├── conf/
       │   ├── gen_py_tool.cfg
       │   ├── gen_py_tool.logo
       │   ├── gen_py_tool_util.cfg
       │   ├── project.yaml
       │   └── template/
       │       ├── gen/
       │       │   ├── editorconfig.template
       │       │   ├── gen_class.template
       │       │   ├── gen_config.template
       │       │   ├── gen_config_util.template
       │       │   ├── gen_logo.template
       │       │   ├── gen_log.template
       │       │   ├── gen_pro_class.template
       │       │   ├── gen_project_yaml.template
       │       │   ├── gen_pro_yaml.template
       │       │   ├── gen_read_template.template
       │       │   ├── gen_run.template
       │       │   ├── gen_write_template.template
       │       │   └── test.template
       │       └── tool/
       │           ├── editorconfig.template
       │           ├── tool_class.template
       │           ├── tool_config.template
       │           ├── tool_config_util.template
       │           ├── tool_logo.template
       │           ├── tool_log.template
       │           └── tool_run.template
       ├── __init__.py
       ├── log/
       │   └── gen_py_tool.log
       ├── pro/
       │   ├── __init__.py
       │   ├── read_template.py
       │   └── write_template.py
       ├── py.typed
       └── run/
           └── gen_py_tool_run.py
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen-py-tool/badge/?version=latest)](https://gen-py-tool.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen_py_tool.readthedocs.io](https://gen-py-tool.readthedocs.io)
* [www.python.org](https://www.python.org/)

### Contributing

[Contributing to gen_py_tool](CONTRIBUTING.md)

### Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2017 - 2024 by [vroncevic.github.io/gen_py_tool](https://vroncevic.github.io/gen_py_tool/)

**gen_py_tool** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
