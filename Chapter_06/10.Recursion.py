# Recursion : -  When Function call itself repeatedly.

# without Recursion print 1 to 5 numbers

def print_num(n):
    print(n)

print_num(1)
print_num(2)
print_num(3)
print_num(4)
print_num(5)

# With Recursion print 1 to 5

def print_n(n):
    if(n == 6): # Base Case (Stoping Condtion)
        return
    print(n)    # Work
    print_n(n+1)    # Function Call

print_n(1)

