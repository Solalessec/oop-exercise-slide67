"""Inheritance - Problem 2.

Person base class, with Student and Employee subclasses that add an
attribute and personalise the introduce method.
"""


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I'm {self.name}, I'm {self.age} and I live in {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)  # reuse the Person constructor
        self.field_of_study = field_of_study

    def introduce(self):
        return f"{super().introduce()} I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"{super().introduce()} I work at {self.company}."


if __name__ == "__main__":
    people = [
        Person("Alice", 40, "Paris"),
        Student("Emma", 20, "Marseille", "Data Science"),
        Employee("Bob", 35, "Lyon", "Airbus"),
    ]
    for person in people:
        print(person.introduce())
