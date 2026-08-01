# Practical Question 6 :
# Que : - Write a program to find the greatest of 3 numbers entered by the user. (With Short Code)

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))    
num3 = int(input("Enter 3rd number : "))

if (num1 > num2) and (num1 > num3):
    print("num1 is Greatest number.")
elif (num2 > num3):
    print("num2 is Greatest number.")
else:
    print("num3 is Greatest number.")