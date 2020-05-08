from setuptools import setup
from commands import ComprehensiveTest, UpdateDocs, GenerateDocs

if __name__ == "__main__":
    setup(
        install_requires = [
            "dataclasses"
        ],
        extras_require = {
            "sphinx": ["sphinx-apidoc", "sphinx-build"],
            "pytest": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd"
            ]
        },
        entry_points = {"console_scripts": []},
        cmdclass = {
            "comprehensiveTest": ComprehensiveTest,
            "updateDocs": UpdateDocs,
            "generateDocs": GenerateDocs
        },
    )
