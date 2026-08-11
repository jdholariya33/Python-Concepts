# del Keyword : - Objects occupy the space in memory, Used to delete object properties or object itself.
#                 For release the memory with delete the unnecessary object and their attributes (properties.

# Syntax : - del obj_name.attribute_name or del obj_name

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Jay")
print(s1.name)

del s1.name

# print(s1.name) --> 'Student' object has no attribute 'name' (Error)

print(s1)

del s1

# print(s1) --> 's1' is not defined (Error)
