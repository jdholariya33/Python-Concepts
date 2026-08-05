# Practical Que 5 :
# Que : - Write a program to check number if number is odd then print "ODD" and if number is even then print "EVEN".

num = int(input("Enter any number : "))

def check_num(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

check_num(num)
