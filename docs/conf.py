import os

project = "yummy_cereal"
author = "Joel Lefkowitz"
copyright = author

master_doc = "modules"
extensions = ["sphinx.ext.napoleon"]

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# Must exclude venv rst files
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]
html_theme = "yummy_sphinx_theme"
