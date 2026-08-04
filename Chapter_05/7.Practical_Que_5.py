# Practical Question 5 :- 
# Que : - Search for a number X in this tuple using loop :
#         (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print("Tuple : ", tup)

x = int(input("Enter a value for searching a number from this tuple: "))

i = 0

while i < len(tup):
    if tup[i] == x:
        print(f"Number {x} at index: ", i)
    else:
        print("Finding...")
    i += 1

