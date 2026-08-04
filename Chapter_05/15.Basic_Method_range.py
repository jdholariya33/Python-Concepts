# Basic methods to write range function :

# Syntax : - range(start?, stop, step?)
# start? (0) and step? (1) are optional but stop is compulsory.

for i in range(10):     # range(stop)
    print(i)            # Output : - 0 to 9 numbers

for i in range(3, 10):     # range(start, stop)
    print(i)            # Output : - 3 to 9 numbers

for i in range(2, 10, 2):     # range(start, stop, step)
    print(i)            # Output : - 2 4 6 8 (even numbers only)

for i in range(1, 10, 2):     # range(start, stop, step)
    print(i)            # Output : - 1 3 5 7 9 (odd numbers only)

