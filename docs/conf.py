import os
import datetime

project = "Yummy Cereal"
author = "Joel Lefkowitz"
copyright = f"{datetime.datetime.now().year}, {author}"
extensions = ["sphinx.ext.napoleon"]

master_doc = 'index'
source_suffix = ['.rst', '.md']
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]

github_url = "github.com/JoelLefkowitz/yummy-cereal"
html_theme = "yummy_sphinx_theme"
html_theme_options = {
    'github_url': github_url,
    'canonical_url': github_url,
    'navbar_icon': 'spin fa-book'
}

napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True

napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False


