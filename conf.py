# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'zoepiran'
copyright = '2023, Zoe Piran'
author = 'Zoe Piran'
release = '0.0.1'
project_name = "ZP"

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
}