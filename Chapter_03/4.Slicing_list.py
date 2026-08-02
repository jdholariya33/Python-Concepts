# Slicing in list :
# Similiar to string slicing, we can slice the list to get a sublist from the original list.

marks = [90, 80, 70, 60, 50] # List of integers

print("List of marks : ", marks)

print("Marks from index 1 to 3 : ", marks[1:4]) # [80, 70, 60]
print("Marks from start to index 2 : ", marks[:3]) # [90, 80, 70]
print("Marks from index 2 to end : ", marks[2:]) # [70, 60, 50]

print("Marks from -4 to -1 :", marks[-4:-1]) # [80, 70, 60]