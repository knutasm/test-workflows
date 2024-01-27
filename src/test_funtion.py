import pytest
from function import add

def test_add_correct():
    assert add(1, 1) == 2


def test_add_failed():
    assert add(2, 2) == 5