# Privte(like) Attributes and Methods : -
# Conceptual Implementations in python :
# Private Attributes and Methods are meant to be used only within the class and are not accessible from outside the class.

# Syntax : __method_name

class Student:
    __name = "anonymous"

    def __hello(self):      # Private Method
        print("hello person!")

    def welcome(self):
        self.__hello()

s1 = Student()

print(s1.welcome())