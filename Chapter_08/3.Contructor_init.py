# __init__ Function : Constructor is basically the init function.
#                     All classes have function called __init__(), which is always executed when the object is being initiated.
#                     Constructor invoke (Execute) at object creation.

# Syntax : - def __init__(self, parameter):
# self : - The self parameter is a reference to the current instance of the class, 
#          and is used to access variables that belongs to the class.

class Student: 
    # Default Constructor
    def __init__(self): # Going with only one constructor
        pass

    # Parameterized Constructor
    def __init__(self, full_name, marks):  # same as (abc, full_name, marks) --> Valid
        self.name = full_name
        self.marks = marks
        print(self) # <__main__.Student object at 0x0000025BC32F8C20> for s1, <__main__.Student object at 0x0000025BC32FCA50> for s2

s1 = Student("Jay", 93)
print(s1)   # <__main__.Student object at 0x0000025BC32F8C20>
print(s1.name)
print(s1.marks)

s2 = Student("Meet", 90)
print(s2)   # <__main__.Student object at 0x0000025BC32FCA50>
print(s2.name , s2.marks)


