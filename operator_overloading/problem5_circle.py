"""Operator overloading - Problem 5.

Circle class with all comparison operators based on the radius.
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, other):   # <
        return self.radius < other.radius

    def __gt__(self, other):   # >
        return self.radius > other.radius

    def __eq__(self, other):   # ==
        return self.radius == other.radius

    def __ne__(self, other):   # !=
        return self.radius != other.radius

    def __ge__(self, other):   # >=
        return self.radius >= other.radius

    def __le__(self, other):   # <=
        return self.radius <= other.radius

    def __repr__(self):
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    small = Circle(2)
    big = Circle(5)
    same = Circle(2)
    print(f"{small} <  {big}: {small < big}")
    print(f"{small} >  {big}: {small > big}")
    print(f"{small} == {same}: {small == same}")
    print(f"{small} != {big}: {small != big}")
    print(f"{small} >= {same}: {small >= same}")
    print(f"{big} <= {small}: {big <= small}")
