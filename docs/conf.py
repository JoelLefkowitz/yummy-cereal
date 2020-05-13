import os
import re
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
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxcontrib.apidoc",
    "sphinxcontrib.napoleon"
]


def relpath(path: str) -> str:
    return os.path.realpath(os.path.join(__file__, path))


def convert_md(source_file: str, target_dir: str) -> None:
    filename = os.path.basename(source_file).replace(".md", ".html")
    output_path = os.path.join(target_dir, filename)
    md = open(source_file, "r").read()

    with open(output_path, "w") as file:
        file.write(pypandoc.convert(md, "html", format="md"))


def remove_heading(path) -> None:
    html = open(path, "r").read()
    with open(path, "w") as file:
        filtered = re.sub("<h1.*>.*?</h1>", "", html, flags=re.DOTALL)
        file.write(filtered)


# Yummy sphinx theme settings
html_theme = "yummy_sphinx_theme"
html_title = "Yummy Cereal"
static_dir = relpath("../static")

html_favicon = os.path.join(static_dir, "favicon.ico")
html_theme_options = {
    "github_url": "JoelLefkowitz/yummy-cereal",
    "navbar_icon": "spin fa-book",
}
html_css_files = [os.path.join(static_dir, "styles.css")]

# Apidoc settings
apidoc_module_dir = relpath("../../yummy_cereal")

# Convert README to html directly
convert_md(relpath("../../README.md"), static_dir)
remove_heading(os.path.join(static_dir, "README.html"))
