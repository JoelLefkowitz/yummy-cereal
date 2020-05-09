from commands import ComprehensiveTest, GenerateDocs, UpdateDocs

from setuptools import setup

if __name__ == "__main__":
    setup(
        install_requires=["dataclasses"],
        extras_require={
            "docs": ["sphinx-apidoc", "sphinx-build"],
            "tests": [
                "pytest",
                "pytest-cov",
                "pytest-html",
                "pytest-sugar",
                "pytest-bdd",
            ],
        },
        entry_points={"console_scripts": []},
        cmdclass={
            "comprehensiveTest": ComprehensiveTest,
            "updateDocs": UpdateDocs,
            "generateDocs": GenerateDocs,
        },
    )
