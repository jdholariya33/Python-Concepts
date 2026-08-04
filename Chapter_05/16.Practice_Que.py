# Practice Question 1 :
# Que : - Using for loop and range method print 1 to 100 numbers.

for i in range(1 , 101, 1):
    print(i)


# Practice Question 2 :
# Que : - Using for loop and range method print 100 to 1 numbers.

for i in range(100, 0, -1):
    print(i)


# Practice Question 3 :
# Que : - Using for loop and range method print the multiplication table of a number n.

n = int(input("Enter any number for print table : "))
for i in range (1, 11):
    print(i * n)