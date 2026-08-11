# 2. Multilevel Inheritance

class Car:      # Parent Class / Base Class    @staticmethod
    def start(self):
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Nissan(Car):     # Child Class / Derived Class
    def __init__(self, brand):
        self.brand = brand

class GTR(Nissan):      # Child class / Derived Class
    def __init__(self, type):
        self.type = type

c1 = GTR("Petrol")

print("Fuel Type", c1.type)

print(c1.start())
