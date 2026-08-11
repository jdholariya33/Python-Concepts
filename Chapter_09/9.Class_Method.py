# Class Method : - A class method is bound to the class & receives the class as an implicit first argument.

# Note : - static method can't access or modify class state & generally for utility.

# Method 1 :
class Person:
    name = "anonymous"

    @classmethod    # decorator
    def changeName(cls, name):
        cls.name = name

"""
    def changeName(self, name):
        #self.name = name   -->     create new variable but not change the anonymous
        #person.name = name -->     Chnage the value from anonymous to Rahul Kumar
        self.__class__.name = "Rahul"
# same self.__Person__.name = "Rahul"
"""

p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

