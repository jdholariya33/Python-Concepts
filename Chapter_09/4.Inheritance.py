# Inheritance : - When one class(child/Derived) derives the properties and  methods of another class(parent/class).

class Car:      # Parent Class / Base Class
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Bmw(Car):     # Child Class / Derived Class
    def __init__(self, name):
        self.name = name

b1 = Bmw("BMW M5")
print("Name of the Car : ")

print("Color of the Car : ", b1.color)

print(b1.start())

print("Reach to the destination, ", b1.stop())

