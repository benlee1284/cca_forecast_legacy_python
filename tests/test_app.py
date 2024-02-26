from src.app import get_average_value
import pytest


def test_get_average_value():
    assert 1 == get_average_value([1])
