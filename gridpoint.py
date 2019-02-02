from __future__ import annotations
import collections
from typing import (
    NamedTuple,
    Tuple,
)


class GridPoint(NamedTuple):
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def is_next_to(self, other: GridPoint) -> bool:
        """与えられた格子点が自身と隣接していればTrueを返す。それ以外はFalse。

        隣接とはある点の上下左右の一方向に一点分動いた位置を言う。
        """
        def is_serial(a: int, b: int) -> bool:
            return abs(a - b) == 1

        return (
            (is_serial(self.x, other.x) and self.y == other.y)
            or (self.x == other.x and is_serial(self.y, other.y))
        )


class GridPoints(collections.UserList):
    def __init__(self, *grid_points: Tuple[GridPoint, ...]) -> None:
        self.data = list(grid_points)

    def connected(self) -> bool:
        """内包するGridPointが隣接している場合にTrueを返す。それ以外はFalse。
        """
        # Stub
        return True
