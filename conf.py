# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from importlib.metadata import metadata
from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

info = metadata("zp")
# info = {
#     "Name": "ZP",
#     "Author": "Zoe Piran",
#     "Version": "0.0.1"
# }
project_name = info["Name"]
author = info["Author"]
copyright = f"{datetime.now():%Y}, {author}"
version = info["Version"]
release = info["Version"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # Our custom extension, only meant for Furo's own documentation.
    # "furo",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

templates_path = ['_templates']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]
suppress_warnings = ['myst.header']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


# html_logo = "_static/img/zp_logo.png"
html_static_path = ["_static"]
html_title = "Zoe Piran"

html_css_files = [
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
      "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]

html_favicon = "_static/img/favicon.ico"

html_theme_options = {
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/zoepiran",
            "html": "",
            "class": "fa-brands fa-github fa-2x",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/zoe_piran",
            "html": "",
            "class": "fa-brands fa-twitter fa-2x"
        },
        {
            "name": "Google-scholar",
            "url": "https://scholar.google.com/citations?user=BlDw0uIAAAAJ&hl=en",
            "html": "",
            "class": "fa-sharp fa-solid fa-graduation-cap fa-2x"
        }
    ],
    "light_css_variables": {
        "color-sidebar-background": "#A7B1A4",
        "color-brand-content": "#5D5A5B",
        "color-background-primary":"#F6F7F5",
        "color-brand-primary": "#5D5A5B"
    },
    "dark_css_variables": {
        "color-sidebar-background": "#A7B1A4",
        "color-brand-content": "#CECDCD",
        "color-background-primary":"#424641",
        "color-brand-primary": "#5D5A5B",
        "color-background-secondary": "#424641",
        "color-background-hover": "#424641"
    },
}