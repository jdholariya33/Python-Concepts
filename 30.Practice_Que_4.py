# Practice Question 4 :
# Que : - Write a program to input 2 integer numbers, a and b.
#         Print True if a is greater than or equal to b. if not print False.

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

# Method 1 :

if a >= b:
    print("True")
    print(f"{a} is greater than or equal to {b}")
else:
    print("False")
    print(f"{a} is lesser than {b}")

# Method 2 :

num = "True" if (a >= b) else "False"
print(num)