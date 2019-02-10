import pytest

import gridpoint


class TestGridPoint2D:
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
    def test_is_next_to(self, a, b):
        assert gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))

    @pytest.mark.parametrize("a, b", [
        ((0, 0), (0, 0)),
        ((1, 1), (0, 0)),
        ((0, -1), (-1, 0)),
    ])
    def test_is_not_next_to(self, a, b):
        assert not gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))


class TestGridPoint3D:
    @pytest.mark.parametrize("x, y, z, expected", [
        (4, 7, 8, "(4, 7, 8)"),
        (-4, -7, -8, "(-4, -7, -8)"),
        (0, 0, 0, "(0, 0, 0)"),
    ])
    def test_string_notation(self, x, y, z, expected):
        assert str(gridpoint.GridPoint(x, y, z)) == expected

    @pytest.mark.parametrize("a, b", [
        ((0, 0, 0), (0, 1, 0)),
        ((0, 0, 0), (1, 0, 0)),
        ((0, 0, 0), (0, 0, 1)),
    ])
    def test_is_next_to(self, a, b):
        assert gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))

    @pytest.mark.parametrize("a, b", [
        ((0, 0, 0), (0, 0, 2)),
        ((0, 1, 0), (1, 1, 1)),
        ((0, -1, 0), (-1, 0, -1)),
    ])
    def test_is_not_next_to(self, a, b):
        assert not gridpoint.GridPoint(*a).is_next_to(gridpoint.GridPoint(*b))


class TestGridPoints2D:
    @pytest.mark.parametrize("a, b", [
        ((0, 0), (0, 1)),
    ])
    def test_contains(self, a, b):
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_a in gridpoints
        assert gridpoint_b in gridpoints

    @pytest.mark.parametrize("a, b, c", [
        ((0, 0), (0, 1), (0, 2)),
    ])
    def test_not_contains(self, a, b, c):
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoint_c = gridpoint.GridPoint(*c)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_c not in gridpoints

    @pytest.mark.parametrize("points", [
        ((0, 0), (0, 1)),
        ((1, 0), (1, 1)),
        ((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 1), (1, 0)),
    ])
    def test_connected(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert gridpoint.GridPoints(*grid_points).connected()

    @pytest.mark.parametrize("points", [
        ((0, 0), (1, 1)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 0), (1, 1), (1, 2)),
    ])
    def test_not_connected(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert not gridpoint.GridPoints(*grid_points).connected()

    @pytest.mark.parametrize("points, expect", [
        ([(0, 0), (0, 1)], 2),
        ([(0, 0), (1, 1), (1, 2)], 3),
    ])
    def test_count_gridpoint(self, points, expect):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert len(gridpoint.GridPoints(*grid_points)) == expect

    @pytest.mark.parametrize("points", [
        ((0, 0), (0, 1), (0, 2), (0, 2)),
    ])
    def test_given_same_gridpoint(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        with pytest.raises(ValueError):
            gridpoint.GridPoints(*grid_points)

    @pytest.mark.parametrize("points", [
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 3), (0, 2), (0, 1)),
        ((0, 0), (1, 0), (1, 1), (1, 2)),
    ])
    def test_is_traversable(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert gridpoint.GridPoints(*grid_points).is_traversable()

    @pytest.mark.parametrize("points", [
        ((0, 0), (0, 1), (0, 2), (0, 4)),
    ])
    def test_is_not_traversable(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert not gridpoint.GridPoints(*grid_points).is_traversable()


class TestGridPoints3D:
    @pytest.mark.parametrize("a, b", [
        ((0, 0, 0), (0, 1, 0)),
    ])
    def test_contains(self, a, b):
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_a in gridpoints
        assert gridpoint_b in gridpoints

    @pytest.mark.parametrize("a, b, c", [
        ((0, 0, 0), (1, 1, 1), (2, 2, 2)),
    ])
    def test_not_contains(self, a, b, c):
        gridpoint_a = gridpoint.GridPoint(*a)
        gridpoint_b = gridpoint.GridPoint(*b)
        gridpoint_c = gridpoint.GridPoint(*c)
        gridpoints = gridpoint.GridPoints(gridpoint_a, gridpoint_b)
        assert gridpoint_c not in gridpoints

    @pytest.mark.parametrize("points", [
        ((0, 0, 0), (0, 1, 0), (0, 2, 0)),
        ((0, 0, 0), (1, 0, 0), (0, 1, 0)),
        ((0, 0, 0), (0, 1, 0), (0, 1, 1)),
        ((0, 0, 0), (0, 1, 0), (1, 0, 0), (0, 0, 1)),
    ])
    def test_connected(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert gridpoint.GridPoints(*grid_points).connected()

    @pytest.mark.parametrize("points", [
        ((0, 0, 0), (0, 1, 0), (0, 1, 2)),
        ((0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0)),
    ])
    def test_not_connected(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert not gridpoint.GridPoints(*grid_points).connected()

    @pytest.mark.parametrize("points", [
        ((0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 1, 2)),
    ])
    def test_is_traversable(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert gridpoint.GridPoints(*grid_points).is_traversable()

    @pytest.mark.parametrize("points", [
        ((0, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 1)),
        ((0, 0, 0), (0, 1, 0), (1, 0, 0), (0, 0, 1)),
    ])
    def test_is_not_traversable(self, points):
        grid_points = (gridpoint.GridPoint(*point) for point in points)
        assert not gridpoint.GridPoints(*grid_points).is_traversable()
