from __future__ import annotations
from typing import NamedTuple


class GridPoint(NamedTuple):
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def is_next_to(self, other: GridPoint) -> bool:
        """与えられた格子点が自身と隣接していればTrueを返す。それ以外はFalse。

        隣接とはある点の上下左右の一方向に一点分動いた位置を言う。
        """
        return (
                (abs(self.x - other.x) == 1 and self.y == other.y)
                or (self.x == other.x and (abs(self.y - other.y) == 1))
        )
