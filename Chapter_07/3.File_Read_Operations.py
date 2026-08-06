# Read Operations in file : 

f = open("D:\VSCode\Python\Chapter 7\info.txt", "r")


# 1. read entire file : - 

data1 = f.read()
print("Read entire file : ", data1)


# 2. read only specific letters of the file : - 

data2 = f.read(9)
print("Read specific amount of letter of the file : ", data2)   # not print a single line from the file....Why ?


# 3. read one line at time : -

data3 = f.readline()
print("Read one line at time : ", data3)
