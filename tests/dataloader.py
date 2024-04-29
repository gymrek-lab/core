import os

import pytest
from pathlib import Path

DATADIR = Path(__file__).parent.joinpath("data")

# functions that all pytests have access to
# Not for use in runtime code!

# Usage based on this documentation
# https://docs.pytest.org/en/latest/example/simple.html#pass-different-values-to-a-test-function-depending-on-command-line-options
def pytest_addoption(parser):
	default = os.path.dirname(os.path.abspath(__file__))
	parser.addoption(
			"--datadir",
			default=default,
			help="Directory containing sample data files"
	)

@pytest.fixture()
def vcfdir(request):
	return DATADIR
