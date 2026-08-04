# range() function : - Range function returns a sequence of numbers, starting from zero by default, 
#                      and increments by 1 (by default), and stops before a specific number. (Important Function)

# syntax : - range(start?, stop, step?)

print(range(5))  # Output :- range(0, 5) such as no output

seq = range(5)
print(seq[0])   # Output : - 0
print(seq[1])   # Output : - 1
print(seq[3])   # Output : - 3

# apply for loop,

seq = range(5)

for i in seq:
    print(i)    # print 0 to 4 numbers (Not Included last digit or number)

# Better Way

for i in range(10):
    print(i)    # print 0 to 9 Numbers (Not Included last digit or number)

