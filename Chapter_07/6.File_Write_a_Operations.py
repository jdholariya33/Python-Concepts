# Writing to a file : 

# Two methods for writing in file : 1. w (write (overwrite)) 2. a (append(and of the file))

# 1. Open File : 

# Syntax : - f = open("File_name", "mode")  --> mode = a (Write over)

f = open("D:\VSCode\Python\Chapter 7\info.txt", "a")


# 2. Write File :

# Syntax : - var = f.write("Data or info")  -->     enter that data at the and of file.

data = f.write("\nCity : Surat\nSkill : Trade")

# 3. Close File
f.close()

# Now Reopen the file : Because the file update successfully but it can't show the data,
#                        so for that we need to close the file and reopen it.

f = open("D:\VSCode\Python\Chapter 7\info.txt", "r")
data = f.read()
print("New data :")
print(data)

f.close()