# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

project = u'gen_py_tool'
copyright = u'2017, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.2.3'
release = u'https://github.com/vroncevic/gen_py_tool/releases'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'classic'
html_static_path = ['_static']
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_py_tool.tex', u'gen\\_py\\_tool Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_py_tool', u'gen_py_tool Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_py_tool', u'gen_py_tool Documentation', author,
    'gen_py_tool', 'One line description of project.', 'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
