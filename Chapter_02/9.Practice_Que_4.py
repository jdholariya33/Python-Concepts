# Practice Question 4 :
# Que : - Write a program to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if num1 > num2:
    if num1 > num3:
        print("num1 is Greatest number.")
    elif num1 < num3:
        print("num3 is Greatest number.")
    else:
        print("num1 and num3 are same.")
        print("num1 and num3 are greatest numbers.")
elif num1 < num2:
    if num2 > num3:
        print("num2 is Greatest number.")
    elif num2 < num3:
        print("num3 is Greatest number.")
    else:
        print("num2 and num3 are same.")
        print("num2 and num3 are greatest numbers.")
elif num1 == num2:
    if num1 < num3:
        print("num1 and num2 are same.")      
        print("num3 is Greatest number.")
    elif num1 > num3:
        print("num1 and num2 are same.")      
        print("num1 and num2 are greatest numbers.")
    else:
        print("num1 , num2 , num3 are same.")
      


