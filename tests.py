import pytest

import gridpoint


class TestGridPoint:
    @pytest.mark.parametrize("x, y, expected", [
        (4, 7, "(4, 7)"),
        (-4, -7, "(-4, -7)"),
        (0, 0, "(0, 0)"),
    ])
    def test_string_notation(self, x, y, expected):
        assert str(gridpoint.GridPoint(x, y)) == expected

    @pytest.mark.parametrize("x, y", [
        (4, 7),
        (-4, -7),
    ])
    def test_equality(self, x, y):
        assert gridpoint.GridPoint(x, y) == gridpoint.GridPoint(x, y)

    @pytest.mark.parametrize("a, b", [
        ((4, 7), (-4, 7)),
        ((4, 7), (4, -7)),
        ((4, 7), (-4, -7)),
    ])
    def test_non_equality(self, a, b):
        assert gridpoint.GridPoint(*a) != gridpoint.GridPoint(*b)

    @pytest.mark.parametrize("a, b", [
        ((0, 0), (0, 1)),
        ((0, 0), (1, 0)),
        ((0, -1), (0, 0)),
    ])
    def test_is_next_to(self, a, b) -> bool:
        assert gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))

    @pytest.mark.parametrize("a, b", [
        ((0, 0), (0, 0)),
        ((1, 1), (0, 0)),
        ((0, -1), (-1, 0)),
    ])
    def test_is_not_next_to(self, a, b) -> bool:
        assert not gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))


class TestGridPoints:
    @pytest.mark.parametrize("a, b", [
        ((0, 0), (0, 1)),
    ])
    def test_contains(self, a, b) -> bool:
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_a in gridpoints
        assert gridpoint_b in gridpoints

    @pytest.mark.parametrize("a, b, c", [
        ((0, 0), (0, 1), (0, 2)),
    ])
    def test_not_contains(self, a, b, c) -> bool:
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoint_c = gridpoint.GridPoint(*c)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_c not in gridpoints
