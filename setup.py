from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=[
            "dataclasses",
            "ruamel.yaml",
            "typing_extensions",
            "typing_inspect",
        ],
        extras_require={
            "dist": ["wheel", "twine", "bump2version"],
            "docs": [
                "sphinx",
                "pypandoc",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
                "sphinx-autodoc-annotation",
                "yummy_sphinx_theme",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
            ],
        },
    )
