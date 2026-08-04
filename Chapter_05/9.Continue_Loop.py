# Continue : - Terminates execution in the current iteration and continue execution of the loop with the next iteration.

i = 0

while i <= 5:
    if(i == 3):
        i += 1
        continue    # Skip the iteration and continue execution of the loop
    print(i)
    i += 1


i = 1
print("Odd Numbers :")

while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1