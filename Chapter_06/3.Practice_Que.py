# Practice Question :
# Que : - Write a program to calculate the average of 3 numbers given by the user using function.

def avg_fun(a, b, c):
    avg = (a + b + c)/3
    return avg

num1 = int(input("Enter 1st Number : "))    
num2 = int(input("Enter 2nd Number : "))    
num3 = int(input("Enter 3rd Number : "))    

res = avg_fun(num1, num2, num3)
print(f"Average of {num1}, {num2} and {num3} : ", res)

