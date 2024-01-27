import pytest
from function import add

def test_add_correct():
    assert add(1, 1) == 2
