# Set : - Set is the collection of the unordered (Not index based) items.
#         Each element in the set must be unique and immutable(elements are immutable).

# Syntax : - set_name = {item1, item2, item3, ...}

Collection = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("Collection : ", Collection)
print("Type of Collection : ", type(Collection))  

Collection = {1, 2, 3, 4, 3, 1, "Python", "Java", "C++", "Python"}

print("Collection : ", Collection)    # ignore the duplicate values
print("Length of Collection : ", len(Collection))    # It counts total number of unique items in the set.

# Empty Set

collection = {} # But it is not a set, it is a dictionary.
print("Type of collection : ", type(collection))  

collection = set() # It is a set.
print("Type of collection : ", type(collection))   

