# Default Parameter in function : 

def cal_mul(a = 2, b = 3):  # If we not pass any default parameter and not any arguments then it shows error
    print(a * b)

cal_mul()   # Without Parameter

def cal_sum(a , b = 3): # Single Default Parameter
    print(a + b)

cal_sum(2)  # Single Argument

def cal_sub(b, a = 7): # Throw Error if b wrote after a (Non-default argument follows default argument) 
    print(a - b)

cal_sub(3)

