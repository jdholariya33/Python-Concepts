# Function : - Block of statements that perform a specific task.
#             Fuction reduce the redundancy(repeatation) of the code.        

# Syntax :-  def func_name(param 1, param2, ...):
#               Some Work

# Function Definition
def calc_sum(a, b):
    sum = a + b
    print("Sum of two numbers : ", sum)
    return sum

# Function Calling : - syntax : - func_name(arg1, arg2, ..)

num1 = int(input("Enter 1st Number : "))    # Argument 1
num2 = int(input("Enter 2nd Number : "))    # Argument 2

result = calc_sum(num1, num2) # Function call



