# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import multiprocessing

project = 'Linux Kernel: Variant from Analog Devices, Inc.'
copyright = '2024, Analog Devices, Inc.'
author = 'Analog Devices, Inc.'
release = 'v6.1'

extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "adi_doctools",
    "myst_parser",
    "sphinx_inline_tabs",
    "sphinxcontrib.mermaid",
    "sphinx.ext.graphviz",
]

needs_extensions = {
    'adi_doctools': '0.3'
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist"
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'

# -- Checks configuration -----------------------------------------------------

linkcheck_allowed_redirects = {
    r"https://ez.analog.com/.*": r"https://ez.analog.com/.*",
    r"https://wiki.analog.com/.*": r"https://wiki.analog.com/.*",
    r"https://analog.com/.*": r"https://analog.com/.*",
    r".*maximintegrated.com/.*": r".*analog.com/.*",
    r"http://.*": r"https://.*",
}

linkcheck_retries = 4

linkcheck_workers = multiprocessing.cpu_count()


# -- External docs configuration ----------------------------------------------

intersphinx_mapping = {
    'doctools': ('https://analogdevicesinc.github.io/doctools', None)
}

# -- Custom extensions configuration ------------------------------------------

hide_collapsible_content = True
validate_links = False

# -- todo configuration -------------------------------------------------------

todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output --------------------------------------------------

html_theme = 'cosmic'
html_static_path = ['sources']
html_css_files = ["custom.css"]
html_favicon = "sources/icon.svg"

# -- Variable substitution ----------------------------------------------------

myst_substitutions = {
    "release_version": "master",
    "release_version_bold": "master",
    "vivado_version": "2021.1",
    "quartus_version": "21.2.0",
    "linux_branch": "master",
    "no_os_branch": "master",
}
rst_prolog = "".join(
    f".. |{key}| replace:: {value}\n" for key, value in myst_substitutions.items()
)