# Practical Question 2 :
# Que : - Search for a number X in this tuple using loop :
#         (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

print("Tuple : ", tup)
X = int(input("Enter any one number for searching in tuple : "))

idx = 0
for el in tup:
    if X == el:
        print("Found at index : ", idx) 
    idx += 1