# 4. Logical Operators (not , and , or)

A = (5 > 4) and (5 > 3)     # and operator with both correct value
print(A)                    # Output : - True

A = (5 > 4) and (5 < 3)     # and operator with one correct and one incorrect value
print(A)                    # Output : - False

A = (5 > 4) or (5 < 3)      # or operator with one correct and one incorrect value
print(A)                    # Output : - True

A = (5 < 4) or (5 < 3)      # and operator with both incorrect value
print(A)                    # Output : - False

A = not(5 < 3)              # not operator with one incorrect value
print(A)                    # Output : - True

A = not(5 > 3)              # not operator with one correct value
print(A)                    # Output : - False


