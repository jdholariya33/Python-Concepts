# 7. Bitwise operators (& , | , ^)

A = 6   # Binary : - 0110
B = 3   # Binary : - 0011

# 1. Bitwise AND  -->  Compare Each bit, returns 1 only if both are 1.
print(A & B)     # Output : - 2  (0010)

# 2. Bitwise OR  -->  Compare Each Bit, return 1 if one or both are 1.
print(A | B)     # Output : - 7  (0111)

# 3. Bitwise XOR  -->  Compare Each Bit, return 1 if the bits are different.
print(A ^ B)     # Output : - 5  (0101)

# 4. Bitwise NOT  -->  Flips all the bits.
print(~A)        # Output : - -7  

# 5. Bitwise Left Shift  -->  Pushes bits to the left.
print(A << 2)    # Output : - 24  (11000)

# 6. Bitwise Right Shift  -->  Pushes bits to the Right.
print(A >> 1)    # Output : - 3   (0011)

