# Call stack in recursion : Call stack is an internal "to-do list" memory structure that tracks active functions.
#                           - In recursion, every time function call itself, 
#                           - Python "Pushes" a new temporary block (stack frame) onto the top of this stack to remember that call's 
#                               variables and current position.

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(3)
