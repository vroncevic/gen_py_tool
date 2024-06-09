Generate Python Tool
---------------------

**gen_py_tool** is package for generation of Python tool.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_py_tool python checker| |gen_py_tool python package| |github issues| |documentation status| |github contributors|

.. |gen_py_tool python checker| image:: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python_checker.yml

.. |gen_py_tool python package| image:: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_py_tool.svg
   :target: https://github.com/vroncevic/gen_py_tool/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_py_tool.svg
   :target: https://github.com/vroncevic/gen_py_tool/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_py_tool/badge/?version=latest
   :target: https://gen_py_tool.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_py_tool python3 build|

.. |gen_py_tool python3 build| image:: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/actions/workflows/gen_py_tool_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_py_tool/releases

To install **gen_py_tool** type the following

.. code-block:: bash

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

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_py_tool

Dependencies
-------------

**gen_py_tool** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
---------------

**gen_py_tool** is based on OOP

Code structure

.. code-block:: bash

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

8 directories, 31 files

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2017 - 2024 by `vroncevic.github.io/gen_py_tool <https://vroncevic.github.io/gen_py_tool>`_

**gen_py_tool** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|Python Software Foundation|

.. |Python Software Foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|Donate|

.. |Donate| image:: https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
