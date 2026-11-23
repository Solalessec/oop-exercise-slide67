"""Operator overloading - Problem 1.

Complex number class with the + and - operators overloaded.
"""


class Complex:
    """A complex number real + imag * i."""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        # (a + bi) - (c + di) = (a - c) + (b - d)i
        return Complex(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"


if __name__ == "__main__":
    z1 = Complex(3, 2)
    z2 = Complex(1, 7)
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    print(f"z1 + z2 = {z1 + z2}")
    print(f"z1 - z2 = {z1 - z2}")
