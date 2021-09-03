# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Cyclone'
copyright = '2021, Jose Fernando Lopez Fernandez'
author = 'Jose Fernando Lopez Fernandez'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# Localization and internationalization options.
#
locale_dirs = [
    'locale/'
]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosummary',
    'sphinx.ext.duration',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'myst_parser',
    'numpydoc',
    'sphinxcontrib.needs',
    'sphinxcontrib.proof',
    'sphinx_rtd_theme'
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for To Do Ext. --------------------------------------------------

# If this is False, the 'to do' and 'to do list' directives produce no output.
# False is the default setting.
#
todo_include_todos = True

# If this is True, each 'to do' directive will trigger a warning. The default is
# False.
#
todo_emit_warnings = False


# -- Options for Numpydoc --------------------------------------------------

numpydoc_use_plots = True
numpydoc_show_class_members = True
numpydoc_class_members_toctree = True
numpydoc_xref_param_type = True

# -- Options for Needs --------------------------------------------------

needs_include_needs = True


# -- Options for To Do Ext. --------------------------------------------------

latex_elements = {
    'preamble': r"""
        \usepackage[utf8]{inputenc}
        \usepackage[T1]{fontenc}
        \usepackage[american]{babel}
        \usepackage{csquotes}
        
        \usepackage{amsmath}
        \usepackage{amsfont}
        \usepackage{amssymb}
        \usepackage{amsthm}
        
        %\theoremstyle{definition}
    """
}

proof_theorem_types = {
    'algorithm': 'Algorithm',
    'conjecture': 'Conjecture',
    'corollary': 'Corollary',
    'definition': 'Definition',
    'example': 'Example',
    'lemma': 'Lemma',
    'proof': 'Proof',
    'property': 'Property',
    'theorem': 'Theorem'
}

math_number_all = True
math_eqref_format = 'Eq.{number}'

numfig = True
numfig_secnum_depth = 1

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'sticky_navigation': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['proof.css']
html_js_files = ['proof.js']
html_show_copyright = True
html_show_sphinx = False
html_math_renderer = 'mathjax'
