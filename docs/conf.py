import os
import datetime
import shutil
import pypandoc
from sphinxcontrib.pandoc_markdown import MarkdownParser


project = "Yummy Cereal"
version = "0.2.5"
author = "Joel Lefkowitz"
copyright = f"{datetime.datetime.now().year}, {author}"

master_doc = "index"
source_suffix = [".rst", ".md"]
source_parsers = {".md": MarkdownParser}
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "venv"]

extensions = [
    "recommonmark",
    "sphinx_markdown_tables",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
]


def relpath(path: str) -> str:
    return os.path.realpath(os.path.join(__file__, path))


def process_md(source_file: str, target_dir: str) -> None:
    filename = os.path.basename(source_file).replace(".md", ".html")
    output_path = os.path.join(target_dir, filename)
    md = open(source_file, "r").read()

    with open(output_path, "w") as file:
        file.write(pypandoc.convert(md, "html", format="md"))


# Yummy sphinx theme settings
html_theme = "yummy_sphinx_theme"
html_title = "Yummy Cereal"
html_favicon = "static/favicon.ico"
html_theme_options = {
    "github_url": "JoelLefkowitz/yummy-cereal",
    "navbar_icon": "spin fa-book",
}

# Apidoc settings
apidoc_module_dir = relpath("../../yummy_cereal")

# Napoleon settings
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

# Copy static files
static_dir = relpath("../static")
process_md(relpath("../../README.md"), static_dir)
