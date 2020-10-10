Generate Python Tool
---------------------

**gen_py_tool** is package for generation of Python tool.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|Python package| |GitHub issues| |Documentation Status| |GitHub contributors|

.. |Python package| image:: https://github.com/vroncevic/gen_py_tool/workflows/Python%20package%20gen_py_tool/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/workflows/Python%20package/badge.svg?branch=master

.. |GitHub issues| image:: https://img.shields.io/github/issues/vroncevic/gen_py_tool.svg
   :target: https://github.com/vroncevic/gen_py_tool/issues

.. |GitHub contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_py_tool.svg
   :target: https://github.com/vroncevic/gen_py_tool/graphs/contributors

.. |Documentation Status| image:: https://readthedocs.org/projects/gen_py_tool/badge/?version=latest
   :target: https://gen_py_tool.readthedocs.io/projects/gen_py_tool/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

Installation
-------------

|Install Python2 Package| |Install Python3 Package|

.. |Install Python2 Package| image:: https://github.com/vroncevic/gen_py_tool/workflows/Install%20Python2%20Package%20gen_py_tool/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/workflows/Install%20Python2%20Package%20gen_py_tool/badge.svg?branch=master

.. |Install Python3 Package| image:: https://github.com/vroncevic/gen_py_tool/workflows/Install%20Python3%20Package%20gen_py_tool/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/workflows/Install%20Python3%20Package%20gen_py_tool/badge.svg?branch=master

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_py_tool/releases

To install **gen_py_tool** type the following:

.. code-block:: bash

    tar xvzf gen_py_tool-x.y.z.tar.gz
    cd gen_py_tool-x.y.z/
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data

You can use Docker to create image/container.

|GitHub docker checker|

.. |GitHub docker checker| image:: https://github.com/vroncevic/gen_py_tool/workflows/gen_py_tool%20docker%20checker/badge.svg
   :target: https://github.com/vroncevic/gen_py_tool/actions?query=workflow%3A%22gen_py_tool+docker+checker%22

Dependencies
-------------

**gen_py_tool** requires next modules and libraries:

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Generation flow of py tool
---------------------------

Base flow of generation process:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/gen_py_tool_flow.png

Tool structure
---------------

**gen_py_tool** is based on OOP:

.. image:: https://raw.githubusercontent.com/vroncevic/gen_py_tool/dev/docs/gen_py_tool.png

Code structure:

.. code-block:: bash

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

Copyright and licence
----------------------

|License: GPL v3| |License: Apache 2.0|

.. |License: GPL v3| image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |License: Apache 2.0| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0

Copyright (C) 2018 by `vroncevic.github.io/gen_py_tool <https://vroncevic.github.io/gen_py_tool>`_

**gen_py_tool** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
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
