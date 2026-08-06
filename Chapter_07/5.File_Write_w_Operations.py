# Writing to a file : 

# Two methods for writing in file : 1. w (write (overwrite)) 2. a (append(and of the file))

# 1. Open File : 

# Syntax : - f = open("File_name", "mode")  --> mode = w (Write over)

f = open("D:\VSCode\Python\Chapter 7\info.txt", "w")


# 2. Write File :

# Syntax : - var = f.write("Data or info")  -->     Overwrite the entire file

data = f.write("Student Profile\n Name: Meet Kanani\nAge: 21\nCourse : Btech IT\nCollege: Indus University\nID: IU2341220171\nCGPA : 6.88\n")

# 3. Close File
f.close()

# Now Reopen the file : Because the file update successfully but it can't show the data,
#                        so for that we need to close the file and reopen it.

f = open("D:\VSCode\Python\Chapter 7\info.txt", "r")
data = f.read()
print("New data :")
print(data)

f.close()