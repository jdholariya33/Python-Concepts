# Expression Execution

# 1. String and Numeric value can operate together with * (Repeat)

A, B = 2 , 3
Txt = "@"
print(A * Txt * B)    # Output :- @@@@@@


# 2. String and String can operate together with + (Concatenation)

A, B = "2", 3
Txt = "@"
print(( A + Txt ) * B)   # Output :- 2@2@2@


# 3. Numeric value can operate together with all Arithmetic operators (+, -, *, /, //, %, **)

A, B = 2, 3
C = 5
print(A + B * C)        # Output :- 17


# 4. Arithmatic expression with integer and float will result in float.

A, B = 2, 3.0
print(A * B)            # Output :- 6.0


# 5. Result of division operator with two integers will be float.

A, B = 1, 2
c = A / B
print(c)                # Output :- 0.5


# 6. Integer division operator (//) with float and int will give int displayed as float.

A, B = 1.5, 3
c = A // B
print(c, A/B)           # Output :- 0.0 0.5


# 7. floor : - Function
# floor gives closest integer, which is lesser than or equal to the float value.
# Result of (A // B) is same as floor(A / B)

A, B = 12 , 5
c = A // B
print(c)                # Output :- 2

A, B = -12 , 5
c = A // B
print(c)                # Output :- -3

A, B = 12 , -5
c = A // B
print(c)                # Output :- -3


# 8. Reminder is negative when denominator is negative. 

A, B = -5, 2
C = A % B
print(C)                # Output :- 1

A, B = 5, 2
C = A % B
print(C)                # Output :- 1

A, B = 5, -2
C = A % B
print(C)                # Output :- -1  

A, B = -5, -2
C = A % B   
print(C)                # Output :- -1