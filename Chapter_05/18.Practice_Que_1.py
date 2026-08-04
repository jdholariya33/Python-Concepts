# Practice Question 1 :
# Que : - Write a program to find the sum of first n numbers.(Using while)

n = int(input("Enter any number : "))
sum = 0
i = 1

while i <= n:
    sum = sum + i    
    i += 1

print(f"Sum of first {n} numbers : ", sum)