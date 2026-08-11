# Super Method :- super() method is used to access methods of the parent class.

class Car:  # Parent Class / Base Class
    def __init__(self, type):
        self.type = type

    def start(self):
        print("Car Started...")

    def stop(self):
        print("Car Stopped...")


class ToyotaCar(Car):  # Child Class / Derived Class
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


c1 = ToyotaCar("prius", "electric")
print(c1.type)