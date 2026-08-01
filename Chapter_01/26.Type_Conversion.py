# Type Conversion  : - Converting one data type to another data type is called type conversion.
"""                    In Python, there are two types of type conversion:
                    1. Implicit Type Conversion (Type conversion) (Done automatically by the interpreter)
                    2. Explicit Type Conversion (Type Casting) (Done manually by the programmer)
"""

a = 10
b = 20.5
sum = a + b     # 10.0 + 20.5 = 30.5   Implicit Type Conversion (Type conversion)
print(sum)  
type(a)  # <class 'int'>

a = "10"
b = 20.5
# sum = a + b      TypeError: can only concatenate str (not "float") to str
a = int(a)  # Explicit Type Conversion (Type Casting)
sum = a + b 
print(sum)
type(a)  # <class 'int'>

a = 3.14

a = str(a) # Explicit Type Conversion (Type Casting)

type(a)  # <class 'str'>