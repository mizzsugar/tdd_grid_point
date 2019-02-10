from __future__ import annotations
import collections
import itertools
from typing import (
    Generic,
    Iterable,
    Iterator,
    Tuple,
    TypeVar,
    Set,
)


T = TypeVar("T", bound=Tuple[int, ...])
U = TypeVar("U", bound="GridPoint")


class GridPoint(tuple, Generic[T]):
    def __new__(cls, *args: int) -> GridPoint[T]:
        return super().__new__(cls, args)

    def __str__(self) -> str:
        return "({})".format(', '.join(str(i) for i in self))

    def is_next_to(self, other: GridPoint[T]) -> bool:
        """与えられた格子点が自身と隣接していればTrueを返す。それ以外はFalse。

        隣接とはある点の上下左右の一方向に一点分動いた位置を言う。
        """
        def is_serial(a: int, b: int) -> bool:
            return abs(a - b) == 1

        def sub(t: Tuple[int, ...], i: int) -> Tuple[int, ...]:
            return t[:i] + t[i + 1:]

        pair: Iterator[Tuple[int, int]] = zip(self, other)
        return any(
            is_serial(element_a, element_b) and sub(self, i) == sub(other, i)
            for i, (element_a, element_b) in enumerate(pair)
        )


class GridPoint2D(GridPoint[Tuple[int, int]]):
    pass


class GridPoint3D(GridPoint[Tuple[int, int, int]]):
    pass


class GridPoints(collections.UserList):
    def __init__(self, *grid_points: Tuple[U, ...]) -> None:
        if len(set(grid_points)) != len(grid_points):
            raise ValueError("Conflict")
        self.data = list(grid_points)

    def connected(self) -> bool:
        """内包する要素のいずれかが他全てと隣接していればTrue。それ以外は
        False。
        """

        def f(point: U, others: Iterable[U]) -> bool:
            return all(point.is_next_to(other) for other in others)

        return any(
            f(point, itertools.chain(self[:i], self[i+1:]))
            for i, point in enumerate(self)
        )

    def is_traversable(self) -> bool:
        """内包する要素が一筆書きできるように隣接していればTrue。
        できなければFalse。
        """
        def f(point: U, others: Set[U]) -> bool:
            if not others:
                return True

            return any(
                point.is_next_to(other) and f(other, others - set([other]))
                for other in others
            )

        points = set(self)
        return any(f(point, points - set(point)) for point in points)
