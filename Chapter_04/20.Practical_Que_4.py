# Practical Question 4 :
# Que : - Figure out a way to store 9 and 9.0 as a separate values in the set.
#         (You can take help of built-in data types)

# Manually stors 9 and 9.0 in set

set1 = {9, 0.9}
print(set1) # 9 and 9.0 is same value and hash value of both are same


# Method 1 :

set1 = {9, "9.0"}
print(set1)


# Method 2 :

value = {
    ("float", 9.0), ("int", 9)
}

print(value)
print(type(value))

