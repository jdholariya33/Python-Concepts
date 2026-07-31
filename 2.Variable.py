# A Token is the smallest individual meaningful unit of code that the interpreter can recognize and process.
# Token :- Variable, Keyword, Identifier, Operator, Punctuation. (5 types of tokens)

# Variable :- Variable is a name that is used to store data in memory.
#             It can hold different types of data such as numbers, strings, lists, etc.

# syntax :- variable_name = value
#  " = " :- Assignment operator.


Name = "Jay Dholariya"  # String Variable (also we wrote value like this 'Jay Dholariya')
age = 20               # Integer Variable
cgpa = 9.44            # Float Variable


# print :- Enter the variable name without quotes.

print(Name)
print("My age is:", age)

CGPA = cgpa # Assigning the value of cgpa to CGPA variable. (Case Sensitive)

print(CGPA)

# print types (Data types) of the variables 

print(type(Name))
print(type(age))
print(type(cgpa))
print(type(CGPA))