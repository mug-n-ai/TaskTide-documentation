# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "TaskTide"
copyright = "2024, Lorenzo Mugnai"
author = "Lorenzo Mugnai"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.githubpages", "sphinx_design", "sphinx_copybutton"]


templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;700&display=swap",  # Sostituisci "Roboto" con il font scelto
    "css/custom.css",
]

# html_logo = "_static/icon.png"
html_favicon = "_static/tasktide.ico"
html_title = "TaskTide"

html_context = {"default_mode": "light"}

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/LorenzoMugnai/TaskTide/tree/master",  # required
            "icon": "fab fa-github-square",
            "type": "fontawesome",
        }
    ]
}

html_copy_source = False
