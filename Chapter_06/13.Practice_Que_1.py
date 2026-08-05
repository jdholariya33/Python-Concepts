# Practicle Question 1 :
# Que : - Write a recursive function to calculate the sum of first n natural numbers.

# num = 5   -->     sum = 1 + 2 + 3 + 4 + 5     -->     sum = sum(4) + 5
# num = n   -->     sum = 1 + 2 + 3 + .. + n    -->     sum = sum(n-1) + n

def calc_num(n):
    if n == 0:
        return 0
    return calc_num(n-1) + n

num = int(input("Enter any number : "))
res = calc_num(num)

print(f"Sum Of first {num} natural numbers : ", res)