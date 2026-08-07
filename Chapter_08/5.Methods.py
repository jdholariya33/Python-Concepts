# Methods : - Methods are functions that belong to objects.

# Syntax : - def method_name(self):
#           For access method  -->  obj_name.method_name() 

class Student:
    College_name = "Indus University"

    def __init__(self, name, marks):    # Constructor
        self.name = name
        self.marks = marks

    def welcome(self):      # Method
        print("Welcome students,", self.name)

    def get_marks(self):    # Method
        return self.marks

s1 = Student("Jay", 93)
s1.welcome()            # Method Call
print(s1.get_marks())   # Method Call
