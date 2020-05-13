import subprocess
from distutils.core import Command


class RunTests(Command):
    description = "Generate a comprehensive test report"
    user_options = [
        ("output=", "o", "Name of report output path [default: test_report.html]")
    ]

    def initialize_options(self) -> None:
        self.output = None

    def finalize_options(self) -> None:
        if self.output is None:
            self.output = ".test_report.html"

    def run(self) -> None:
        subprocess.run(
            [
                "pytest",
                "--cov",
                "yummy_cereal",
                "--html",
                self.output,
                "--self-contained-html",
            ]
        )


class BuildDocs(Command):
    description = "Sphinx build"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-build", "docs/", "build/"])
