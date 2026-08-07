# Attributes : - Data or Variable

# Class Attribute : - Common for all the objects of the class
# Instance Attribute : - Different according to object 

class Student: 
    College_name = "Indus University"   # Class Attribute
    name = "anonymous"  # Class Attribute

    def __init__(self, name, marks):  #  precedence :- Obj attr > Class attr
        self.name = name    # Instance (Object) Attribute --> self is used for instance attribute because it is reffrence of the objet.
        self.marks = marks

s1 = Student("Jay", 93)
print(s1.name, s1.marks)
print(s1.College_name)

s2 = Student("Meet", 90)
print(s2.name , s2.marks)
print(Student.College_name)
