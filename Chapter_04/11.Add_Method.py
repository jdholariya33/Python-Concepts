# 1. Add Method : - The add() method adds an element to the set. If the element already exists, it will not be added again.

set1 = {1, 2, 3, 4, 5}

set1.add(6)    # Adding an element to the set
print("Set After Adding Element : ", set1)    # Add 6 at the end of the set.

set1.add(3)    # Adding an existing element to the set
print("Set After Adding Existing Element : ", set1)    # It will not add 3.

set1.add("Python")    # Adding a string element to the set
print("Set After Adding String Element : ", set1)    # It will add "Python".

set1.add((1, 2, 3))    # Adding a tuple element to the set
print("Set After Adding Tuple Element : ", set1)    # It will add (1, 2, 3).
