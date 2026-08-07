# Encapsulation : - Wrapping data and functions into a single unit(object).

class Student:
    def __init__(self, name):   
        self.name = name    # Data

    def hello(self):    # Method / Function
        print("Hello,", self.name)

s1 = Student("Jay") # object (Wrapping into a single unit.)
s1.hello()  