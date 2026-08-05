# Practical Question 2 :
# Que : - Write a function to find the factorial of n. (n is the parameter)

n = int(input("Enter any number for print its factorial : "))

def cal_fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print(f"Factorial of given number {num} : ", fact)

cal_fact(n)