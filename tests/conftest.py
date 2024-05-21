# content of tests/conftest.py
import numpy
import pytest


@pytest.fixture(autouse=True)
def add_np_namespace():
    import builtins
    builtins.np = numpy
