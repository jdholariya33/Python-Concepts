# Tuple : - A Built-in data type that lets us create immutable sequences of values. (Similiar to string)

tup = (1, 2, 3, 4)
print(tup)  # Output : - (1, 2, 3, 4)
print(type(tup))    # Output : - <class 'tuple'>

# Tuple is immutable :

# tup[0] = 1    -->     'tuple' object does not support item assignment

# Empty Tuple :

tup = ()
print(tup)  # Output : - ()
print(type(tup))    # Output : - <class 'tuple'>

# Tuple with single Value :

tup = (1, )
print(tup)  # Output : - (1,)
print(type(tup))    # Output : - <class 'tuple'>

tup = (1)
print(tup)  # Output : - 1
print(type(tup))    # Output : - <class 'int'>

