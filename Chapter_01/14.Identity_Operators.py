# 6. Identity Operators (is, is not)

list_a = [1 , 2 , 3]
list_b = [1 , 2 , 3]

list_c = list_a

print(list_a is list_c)        # Output : - True (They Share the same memory location)
print(list_a is list_b)        # Output : - False (Different Object, even though values match)

print(list_a is not list_b)    # Output : - True
print(list_a is not list_c)    # Output : - False

print(list_a == list_b)        # Output : - True (Values are identical)

