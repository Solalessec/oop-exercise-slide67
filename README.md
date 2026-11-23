# OOP exercises - Slide 67

Python solutions to the "OOP Problems" exercise sheet (OOP course, AIDAMS 2A):
operator overloading and inheritance.

## Structure

```
oop-exercise-slide67/
├── operator_overloading/
│   ├── problem1_complex.py      # + and - for complex numbers
│   ├── problem2_person.py       # > compares two persons by age
│   ├── problem4_vector.py       # * returns the dot product of two 3D vectors
│   ├── problem5_circle.py       # <, >, ==, !=, >=, <= based on the radius
│   ├── problem6_point.py        # comparisons by distance from the origin
│   └── problem7_matrix.py       # * multiplies two matrices
├── inheritance/
│   ├── problem1_vehicle.py      # Vehicle -> Car, Bicycle (method override)
│   ├── problem2_person.py       # Person -> Student, Employee (super())
│   └── problem3_bank_account.py # BankAccount -> SavingsAccount, transfer()
└── test_all.py                  # one test per problem
```

The exercise sheet has no Problem 3 in the operator overloading part, so the numbering follows the sheet.

## How to run

Each file runs on its own and prints a short demo:

```bash
python3 operator_overloading/problem1_complex.py
python3 inheritance/problem3_bank_account.py
```

Run all the tests:

```bash
python3 test_all.py
# or, if pytest is installed
pytest
```

## Key ideas

### Operator overloading
Python calls a "magic method" when an operator is used on an object:

| Operator | Method called |
|---|---|
| `a + b` | `a.__add__(b)` |
| `a - b` | `a.__sub__(b)` |
| `a * b` | `a.__mul__(b)` |
| `a < b`, `a > b` | `a.__lt__(b)`, `a.__gt__(b)` |
| `a <= b`, `a >= b` | `a.__le__(b)`, `a.__ge__(b)` |
| `a == b`, `a != b` | `a.__eq__(b)`, `a.__ne__(b)` |

Defining these methods in a class tells Python what the operator means for that class.

### Inheritance
- `class Car(Vehicle)` means Car inherits all the attributes and methods of Vehicle.
- **Override**: a subclass redefines a method of its parent (`Car.drive()` replaces `Vehicle.drive()`).
- **`super()`** calls the parent's version, e.g. `super().__init__(name, age, address)` reuses the Person constructor in Student.
- **Polymorphism**: the same call (`vehicle.drive()`) gives a different result depending on the object's class.
