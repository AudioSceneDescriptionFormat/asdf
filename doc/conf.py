# Configuration file for the Sphinx documentation builder.

project = 'ASDF'
author = 'Matthias Geier'
copyright = '2018, ' + author

# needs_sphinx = '1.0'

extensions = [
]

master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
highlight_language = 'xml'
pygments_style = None


# -- Get version information and date from Git ----------------------------

try:
    from subprocess import check_output
    release = check_output(['git', 'describe', '--tags', '--always'])
    release = release.decode().strip()
    today = check_output(['git', 'show', '-s', '--format=%ad', '--date=short'])
    today = today.decode().strip()
except Exception:
    release = '<unknown>'
    today = '<unknown date>'


# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
# html_theme_options = {}


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'printindex': '',
    'preamble': r"""
\usepackage[sc,osf]{mathpazo}
\linespread{1.05}  % see http://www.tug.dk/FontCatalogue/urwpalladio/
\renewcommand{\sfdefault}{pplj}  % Palatino instead of sans serif
\IfFileExists{zlmtt.sty}{
    \usepackage[light,scaled=1.05]{zlmtt}  % light typewriter font from lmodern
}{
    \renewcommand{\ttdefault}{lmtt}  % typewriter font from lmodern
}
""",
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'asdf.tex', project, author, 'howto'),
]

latex_show_urls = 'footnote'

# -- Options for Epub output -------------------------------------------------

epub_title = project
epub_exclude_files = ['search.html']
