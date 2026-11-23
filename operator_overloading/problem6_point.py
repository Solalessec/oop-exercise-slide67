"""Operator overloading - Problem 6.

2D Point class compared by Euclidean distance from the origin:
distance = sqrt(x^2 + y^2)
"""

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # All comparisons use the distance from the origin (0, 0)
    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __ne__(self, other):
        return self.distance_from_origin() != other.distance_from_origin()

    def __le__(self, other):
        return self.distance_from_origin() <= other.distance_from_origin()

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    p1 = Point(3, 4)   # distance 5
    p2 = Point(1, 1)   # distance ~1.41
    p3 = Point(-4, 3)  # distance 5
    print(f"{p1}: distance {p1.distance_from_origin():.2f}")
    print(f"{p2}: distance {p2.distance_from_origin():.2f}")
    print(f"{p1} > {p2}: {p1 > p2}")
    print(f"{p1} == {p3}: {p1 == p3}")
    print(f"{p2} <= {p3}: {p2 <= p3}")
