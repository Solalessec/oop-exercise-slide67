"""Operator overloading - Problem 2.

Person class where p1 > p2 compares the two persons by age.
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __gt__(self, other):
        # p1 > p2 is True when p1 is older than p2
        return self.age > other.age

    def __repr__(self):
        return f"Person({self.name}, {self.age}, {self.gender})"


if __name__ == "__main__":
    alice = Person("Alice", 30, "F")
    bob = Person("Bob", 25, "M")
    print(f"{alice.name} > {bob.name}: {alice > bob}")  # True
    print(f"{bob.name} > {alice.name}: {bob > alice}")  # False
