# Practical Question 3 :
# Que : - Write a program to enter marks of 3 subjects from the user and store them in a dictionary.
#         Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

marks = { }

x = int(input("Enter marks of physics : "))
marks["physics"] = x

y = int(input("Enter marks of chemistry : "))
marks.update({"chemistry" : y})

z = int(input("Enter marks of mathematics : "))
marks["mathematics"] = z

print(marks)