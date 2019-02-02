import pytest

import gridpoint


@pytest.mark.parametrize("x, y, expected", [
    (4, 7, "(4, 7)"),
    (-4, -7, "(-4, -7)"),
    (0, 0, "(0, 0)"),
])
def test_string_notation(x, y, expected):
    assert str(gridpoint.GridPoint(x, y)) == expected


@pytest.mark.parametrize("x, y", [
    (4, 7),
    (-4, -7),
])
def test_equality(x, y):
    assert gridpoint.GridPoint(x, y) == gridpoint.GridPoint(x, y)


@pytest.mark.parametrize("a, b", [
    ((4, 7), (-4, 7)),
    ((4, 7), (4, -7)),
    ((4, 7), (-4, -7)),
])
def test_non_equality(a, b):
    assert gridpoint.GridPoint(*a) != gridpoint.GridPoint(*b)


@pytest.mark.parametrize("a, b", [
    ((0, 0), (0, 1)),
    ((0, 0), (1, 0)),
    ((0, -1), (0, 0)),
])
def test_is_next_to(a, b) -> bool:
    assert gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))


@pytest.mark.parametrize("a, b", [
    ((0, 0), (0, 0)),
    ((1, 1), (0, 0)),
    ((0, -1), (-1, 0)),
])
def test_is_not_next_to(a, b) -> bool:
    assert not gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))
