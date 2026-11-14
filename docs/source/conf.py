# -*- coding: UTF-8 -*-

'''
Module
    conf.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_py_tool is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_py_tool is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines properties for sphinx-doc.
'''

from __future__ import annotations

from os.path import abspath
from sys import path

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_py_tool/blob/dev/LICENSE'
__version__ = '1.4.2'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

path.insert(0, abspath('../../'))

project: str = 'gen_py_tool'
project_copyright: str = '2026, Vladimir Roncevic <elektron.ronca@gmail.com>'
author: str = 'Vladimir Roncevic <elektron.ronca@gmail.com>'
version: str = '1.4.2'
release: str = 'https://github.com/vroncevic/gen_py_tool/releases'
extensions: list[str] = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path: list[str] = ['_templates']
source_suffix: str = '.rst'
root_doc: str = 'index'
language: str = 'en'
exclude_patterns: list[str] = []
pygments_style: str = 'sphinx'
html_theme: str = 'classic'
html_static_path: list[str] = ['_static']
htmlhelp_basename: str = 'gen_py_tooldoc'
latex_elements: dict[object, object] = {}
latex_documents: list[tuple[object, ...]] = [(
    root_doc, 'gen_py_tool.tex', 'gen_py_tool Documentation',
    'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages: list[tuple[object, ...]] = [(
    root_doc, 'gen_py_tool', 'gen_py_tool Documentation', [author], 1
)]
texinfo_documents: list[tuple[object, ...]] = [(
    root_doc, 'gen_py_tool', 'gen_py_tool Documentation', author, 'gen_py_tool',
    'Python tool project setup generator.', 'Miscellaneous'
)]
epub_title: str = project
epub_exclude_files: list[str] = ['search.html']
