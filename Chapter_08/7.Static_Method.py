# Static Method : - Methods that don't use the self parameter (work at class level)

class Student:
    def __init__(self, name):
        self.name = name

    @staticmethod   # Decorator
    def hello():
        print("hello")

# Decorator : - Allows us to wrap another function in order to extend the behaviour of the wrapped function, 
#               without permanently modifying it.

s1 = Student("Jay")
s1.hello()
