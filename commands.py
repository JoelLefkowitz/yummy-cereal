import subprocess
from distutils.core import Command


class ComprehensiveTest(Command):
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


class UpdateDocs(Command):
    description = "Update build configuration using sphinx-apidoc"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-apidoc", "-o", "docs/", "yummy_cereal/", "tests/"])


class GenerateDocs(Command):
    description = "Generate docs using sphinx-autodoc"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-build", "docs/", "build/"])
