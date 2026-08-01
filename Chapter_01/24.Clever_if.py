# Clever if / Ternary Operator

# Syntax : - <var> = (false_value, true_value)[condition]

# without using ternary operator

print("if-else Statement")

age = int(input("Enter your age : "))
if age >= 18:
    print("Able to vote")
else:
    print("Not Able to vote")

# using ternary operator

print("Ternary Operator / Clever if")

age = int(input("Enter your age : "))
status = ("Not Able to vote", "Able to vote")[age >= 18]
print(f"Status : {status}")


sal = int(input("Enter your salary : "))
tax = sal*(0.1, 0.2)[sal >= 50000]
print(f"Tax : {tax}")