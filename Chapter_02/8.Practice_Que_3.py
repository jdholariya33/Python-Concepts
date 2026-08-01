# Practice Question 3 :
# Que : - Write a program to check if a number enterd by the user is odd or even.

num = int(input("Enter any number : "))

if num % 2 == 0:
    print(f"{num} is even number.")
elif num % 2 != 0:
    print(f"{num} is odd number.")
else:
    print("Please enter valid input.")

print("End of code..!")