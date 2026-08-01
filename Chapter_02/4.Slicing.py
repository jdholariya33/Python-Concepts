# Slicing : - Accessing parts of the String
# Syntax : - str[starting_idx : ending_idx]     -->     ending index is not included in part of the string

str = "How Are you, Welcome..!"

print(str[2 : 5])   # Output :- W A
print(str[  : 8])   # Output :- How Are     -->     as str[0 : 8]
print(str[3 :  ])   # Output :-  Are you, Welcome..!    -->     as str[3 : len(str)]

# Negative Indexing

str = "Apple is a fruit"

print(str[-15 : -3]) # Output : - pple is a fr  
print(str[-4 :    ]) # Output : - ruit      -->     as str[-4 : -1]
print(str[   :  -2]) # Output : - Apple is a fru    -->     as str[-len(str) : -2]
