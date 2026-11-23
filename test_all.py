"""Tests for every problem. Run with: python3 test_all.py  (or: pytest)"""

import importlib.util
import math
import sys
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "operator_overloading"))
sys.path.insert(0, str(ROOT / "inheritance"))

import problem1_complex as complex_mod
import problem4_vector as vector_mod
import problem5_circle as circle_mod
import problem6_point as point_mod
import problem7_matrix as matrix_mod
import problem1_vehicle as vehicle_mod
import problem3_bank_account as bank_mod


# problem2_person.py exists in both folders: load each one from its path
def load(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


person_cmp = load("operator_overloading/problem2_person.py", "person_cmp")
person_mod = load("inheritance/problem2_person.py", "person_inh")


# ---------------- Operator overloading ----------------

def test_complex_add_sub():
    z1, z2 = complex_mod.Complex(3, 2), complex_mod.Complex(1, 7)
    assert z1 + z2 == complex_mod.Complex(4, 9)
    assert z1 - z2 == complex_mod.Complex(2, -5)


def test_person_greater_than():
    old, young = person_cmp.Person("A", 30, "F"), person_cmp.Person("B", 25, "M")
    assert (old > young) is True
    assert (young > old) is False


def test_vector_dot_product():
    assert vector_mod.Vector(1, 2, 3) * vector_mod.Vector(4, 5, 6) == 32


def test_circle_comparisons():
    small, big, same = circle_mod.Circle(2), circle_mod.Circle(5), circle_mod.Circle(2)
    assert small < big and big > small
    assert small == same and small != big
    assert small >= same and small <= same and not big <= small


def test_point_distance_comparisons():
    p1, p2, p3 = point_mod.Point(3, 4), point_mod.Point(1, 1), point_mod.Point(-4, 3)
    assert math.isclose(p1.distance_from_origin(), 5)
    assert p1 > p2 and p2 < p1
    assert p1 == p3 and p1 != p2
    assert p2 <= p3 and p3 >= p1


def test_matrix_multiplication():
    a = matrix_mod.Matrix([[1, 2], [3, 4]])
    b = matrix_mod.Matrix([[5, 6], [7, 8]])
    assert a * b == matrix_mod.Matrix([[19, 22], [43, 50]])
    # 2x3 * 3x1 -> 2x1
    c = matrix_mod.Matrix([[1, 2, 3], [4, 5, 6]])
    d = matrix_mod.Matrix([[1], [0], [2]])
    assert c * d == matrix_mod.Matrix([[7], [16]])


def test_matrix_incompatible_sizes():
    a = matrix_mod.Matrix([[1, 2]])
    try:
        a * a
    except ValueError:
        return
    raise AssertionError("ValueError expected")


# ---------------- Inheritance ----------------

def test_vehicle_override():
    assert vehicle_mod.Vehicle().drive() == "Driving a vehicle"
    assert vehicle_mod.Car().drive() == "Driving a car"
    assert vehicle_mod.Bicycle().drive() == "Riding a bicycle"
    assert isinstance(vehicle_mod.Car(), vehicle_mod.Vehicle)


def test_person_student_employee():
    student = person_mod.Student("Emma", 20, "Marseille", "Data Science")
    employee = person_mod.Employee("Bob", 35, "Lyon", "Airbus")
    assert isinstance(student, person_mod.Person)
    assert student.name == "Emma" and student.field_of_study == "Data Science"
    assert "Data Science" in student.introduce()
    assert "Airbus" in employee.introduce()
    assert "Emma" in student.introduce()


def test_bank_account_and_transfer():
    current = bank_mod.BankAccount("FR-001", 500)
    savings = bank_mod.SavingsAccount("FR-002", 1000, interest_rate=0.05)
    current.deposit(200)
    current.withdraw(100)
    assert current.balance == 600
    assert current.transfer(savings, 250) is True
    assert current.balance == 350 and savings.balance == 1250
    assert current.transfer(savings, 5000) is False
    assert current.balance == 350  # nothing moved
    assert math.isclose(savings.add_interest(), 62.5)
    assert math.isclose(savings.check_balance(), 1312.5)
    assert isinstance(savings, bank_mod.BankAccount)


if __name__ == "__main__":
    tests = [f for name, f in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
        print(f"PASS  {test.__name__}")
    print(f"\nAll {len(tests)} tests passed.")
