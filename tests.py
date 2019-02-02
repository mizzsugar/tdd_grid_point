import pytest

import gridpoint


@pytest.mark.parametrize("x, y, expected", [
    (4, 7, "(4, 7)"),
    (-4, -7, "(-4, -7)"),
    (0, 0, "(0, 0)"),
])
def test_string_notation(x, y, expected):
    assert str(gridpoint.GridPoint(x, y)) == expected
