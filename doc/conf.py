# Configuration file for the Sphinx documentation builder.

project = 'ASDF'
author = 'Matthias Geier'
copyright = '2018, ' + author

# needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.todo',
    'nbsphinx',
]

todo_include_todos = True

master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']
highlight_language = 'xml'
pygments_style = None

rst_prolog = """
.. |asdf| replace:: ``<asdf>``
.. |head| replace:: ``<head>``
.. |meta| replace:: ``<meta>``
.. |source| replace:: ``<source>``
.. |reference| replace:: ``<reference>``
.. |body| replace:: ``<body>``
.. |seq| replace:: ``<seq>``
.. |par| replace:: ``<par>``
.. |clip| replace:: ``<clip>``
.. |channel| replace:: ``<channel>``
.. |transform| replace:: ``<transform>``
.. |o| replace:: ``<o>``
"""

nbsphinx_prolog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{ docname }}`__.
        Interactive online version: :raw-html:`<a href="https://mybinder.org/v2/gh/AudioSceneDescriptionFormat/asdf/{{ env.config.release }}?filepath={{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/AudioSceneDescriptionFormat/asdf/blob/
        {{ env.config.release }}/{{ docname }}

.. raw:: latex

    \nbsphinxstartnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{The following section was generated from
    \sphinxcode{\sphinxupquote{\strut {{ docname | escape_latex }}}} \dotfill}}
"""

nbsphinx_epilog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}

.. raw:: latex

    \nbsphinxstopnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{\dotfill\ \sphinxcode{\sphinxupquote{\strut
    {{ docname | escape_latex }}}} ends here.}}
"""

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
html_sourcelink_suffix = ''
html_scaled_image_link = False
html_add_permalinks = '\N{SECTION SIGN}'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'printindex': '',
    'sphinxsetup': r"""
        VerbatimColor={HTML}{F5F5F5},
        VerbatimBorderColor={HTML}{E0E0E0},
        noteBorderColor={HTML}{E0E0E0},
        noteborder=1.5pt,
        warningBorderColor={HTML}{E0E0E0},
        warningborder=1.5pt,
        warningBgColor={HTML}{FBFBFB},
    """,
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
latex_show_pagerefs = True

# -- Options for Epub output -------------------------------------------------

epub_title = project
epub_exclude_files = ['search.html']
