# File's Basic operation :

# 1. Open File : 

# Syntax : - f = open("File_name", "mode")  --> mode = r (read by default)

f = open("D:\VSCode\Python\Chapter 7\info.txt", "r")


# 2. Read File :

# Syntax : - var = f.read()

data = f.read()
print(data)
print(type(data))


# 3. Close File

# Syntax : - f.close()

f.close()
