# Basic Operations 
# List is Mutable, We can access, modify, add and delete elements from the list.

Student = ["Meet" , 21, 5.8, "Male"] # List of different data types

# Accessing elements from the list

print("Student details : ", Student)
print("Name : ", Student[0]) # Meet
print("Age : ", Student[-3]) # 21


# Modifying elements in the list

Student[0] = "Krisha"
Student[-1] = "Female"
print("Modified Student details : ", Student)


# Adding elements to the list

Student.append("B.Tech") # Adding element at the end of the list
print("Student details after adding course : ", Student)



# Inserting elements to the list at a specific index

Student.insert(2, 9.32) # Inserting element at index 2
print("Student details after inserting CGPA : ", Student)


# Deleting elements from the list

Student.remove(21) # Removing element by value
print("Student details after removing age : ", Student)

Student.pop(1) # Removing element by index
print("Student details after removing CGPA : ", Student)