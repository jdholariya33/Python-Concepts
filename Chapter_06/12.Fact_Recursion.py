# Factorial using recursion :
# n! = 1 * 2 * 3 * ... * (n-1) * n      -->     n! = (n-1)! * n     -->     Recurrence Relation
# 4! = 1 * 2 * 3 * 4                    -->     4! = (3)! * 4
# 3! = 1 * 2 * 3                        -->     3! = (2)! * 3
# 2! = 1 * 2                            -->     2! = (1)! * 2
# 1! = 1          

def fact(n):
    if (n == 0 or n == 1):
        return 1
    return fact(n-1) * n

num = int(input("Enter any number that you want to find factorial : "))
fact = fact(num)

print(f"Factorial of {num} : ", fact)