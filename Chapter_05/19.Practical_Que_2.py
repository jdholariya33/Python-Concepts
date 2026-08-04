# Practical Question 2 :
# Que : - Write a program to find the factorial of first n natural numbers. (Using for)

# Factorial : - n! = n * (n-1) * (n-2) * (n-3) * ... * 1
# Example : - 3! = 3 * 2 * 1 = 6
#             5! = 5 * 4 * 3 * 2 * 1 = 120

n = int(input("Enter any number : "))
fact = 1

for i in range(n, 0, -1):
    fact *= i
    i -= 1

print(fact)    
