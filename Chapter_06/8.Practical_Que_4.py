# Practical Question 4 :
# Que : - Write a function to convert USD to INR.

"""
1 USD --> 95.39 INR
num USD --> ? INR

num USD * 95.39 INR = 1 USD * ? INR
? INR = num USD * 95.39 / 1 USD
? = num * 95.39
"""

USD = int(input("Enter USD for convert it into INR : "))

def USD_INR(num):
    rupee = num * 95.39     # Current rate of 1 USD
    print(f"{num} USD equal to {rupee} Rs.")

USD_INR(USD)
