from src.app import get_average_value
from typing import Union
import pytest


@pytest.mark.parametrize(
    "values, decimal_places, expected_result",
    [
        ([1, 2, 3, 4, 5], None, 3),
        ([1.1, 2.2, 3.3, 4.4, 5.5], 2, 3.3),
    ]
)
def test_get_average_value(
        values: list[Union[float, int]],
        decimal_places: Union[int, None],
        expected_result: Union[int, float],
) -> None:
    assert expected_result == get_average_value(values, decimal_places)
