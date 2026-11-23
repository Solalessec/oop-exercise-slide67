"""Inheritance - Problem 1.

Vehicle base class, with Car and Bicycle overriding the drive method.
"""


class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):  # override
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):  # override
        return "Riding a bicycle"


if __name__ == "__main__":
    # Polymorphism: same method call, different behaviour depending on the class
    for vehicle in [Vehicle(), Car(), Bicycle()]:
        print(f"{type(vehicle).__name__}: {vehicle.drive()}")
