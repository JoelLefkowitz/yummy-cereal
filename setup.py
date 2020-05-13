from commands import RunTests, BuildDocs
from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["dataclasses", "pyimport"],
        extras_require={
            "dist": ["wheel"],
            "docs": [
                "sphinx",
                "recommonmark",
                "sphinx_markdown_tables",
                "sphinxcontrib.apidoc",
                "sphinxcontrib.pandoc_markdown",
            ],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
            ],
        },
        entry_points={"console_scripts": []},
        cmdclass={"tests": RunTests, "docs": BuildDocs,},
    )
