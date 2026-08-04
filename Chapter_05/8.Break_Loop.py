# Break : - Used to terminate the loop when encountered.

i = 0

while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("End of the loop..")

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print("Tuple : ", tup)

x = int(input("Enter a value for searching a number from this tuple: "))

i = 0

while i < len(tup):
    if tup[i] == x:
        print(f"Number {x} at index: ", i)
        break
    else:
        print("Finding...")
    i += 1