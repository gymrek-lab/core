"""Nox sessions."""
import os
import shutil
from pathlib import Path

import nox
from nox_poetry import Session
from nox_poetry import session


package = "core"
python_versions = ["3.7", "3.8", "3.9", "3.10", "3.11", "3.12"]
locked_python_version = "3.8"
nox.needs_version = ">= 2022.11.21"
nox.options.sessions = (
    "docs",
    "tests",
    "lint",
)


cov_cli_args = [
    "--cov=.",
    "--cov-report=term-missing",
]


@session(python=locked_python_version)
def docs(session: Session) -> None:
    """Build the documentation."""
    args = session.posargs or ["docs", "docs/_build"]
    if not session.posargs and "FORCE_COLOR" in os.environ:
        args.insert(0, "--color")

    build_dir = Path("docs", "_build")
    if build_dir.exists():
        shutil.rmtree(build_dir)

    session.run("sphinx-build", *args)


@session(python=locked_python_version)
def lint(session: Session) -> None:
    """Lint our code."""
    session.install("black")
    session.run("black", "--verbose", "--check", ".")


def install_handle_python(session):
    """
    handle incompatibilities between python and other packages
    see https://github.com/cjolowicz/nox-poetry/issues/1116
    """
    # install the latest versions of all dependencies for py3.9+
    # but install the locked versions for < py3.9 to ensure some stability in the CI and
    # help us understand when we need to bump our version constraints
    if session._session.python in ("3.9", "3.10", "3.11", "3.12"):
        session._session.install(".")
    else:
        session.install(".")


# detect whether conda/mamba is installed
if os.getenv("CONDA_EXE"):
    conda_cmd = "conda"
    if (Path(os.getenv("CONDA_EXE")).parent / "mamba").exists():
        conda_cmd = "mamba"
    conda_args = ["-c", "conda-forge"]

    @session(venv_backend=conda_cmd, venv_params=conda_args, python=python_versions)
    def tests(session: Session) -> None:
        """Run the test suite."""
        session.conda_install(
            "numpy",
            "pytest",
            "pytest-cov",
            channel="conda-forge",
        )
        install_handle_python(session)
        session.run("python", "-m", "pytest", *cov_cli_args, *session.posargs)

else:

    @session(python=python_versions)
    def tests(session: Session) -> None:
        """Run the test suite."""
        session.install("pytest", "pytest-cov")
        install_handle_python_numpy(session)
        session.run("python", "-m", "pytest", *cov_cli_args, *session.posargs)
