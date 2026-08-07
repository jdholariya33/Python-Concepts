# Class and Object :

# 1. Class : - Class is a blueprint for creating objects.
#              Class is collection of data(Attributes) and Methods. 
# Syntax : - class Class_name:      -->     Class name always start with capital letter.

class Student:
    name = "Jay Dholariya"


# 2. Object : - Object is instance of the class.

# Syntax : - obj_name = Class_name()

s1 = Student()
print(s1)
print(s1.name)

s2 = Student()
print(s2.name)

# Exaple  : Car

class Car:
    color = "blue"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)

