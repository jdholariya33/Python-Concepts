# Types Of Inheritance : 

# 1. Single Inheritance

class Person:       # Parent class 
    def excercise(self):
        print("Running..")

    def eat(self):
        print("Eat some food.")

    gender = "Male"
    country = "India"

class Student(Person):      # Child Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Meet", 20)
print("Name : ", s1.name)
print("Age : ", s1.age)

print("Gender : ", s1.gender)
print("Country : ", s1.country)

print(s1.excercise())
print(s1.eat())