# Practical Question 3 :
# Que : - Print the multiplication table of a number n.


n = int(input("Enter any number : "))

i = 1

print(f"Table of {n} : ")

while i <= 10:
    print(f"{n} * {i} =", n * i )
    i += 1


