# Read Operations in file : 

f = open("D:\VSCode\Python\Chapter 7\info.txt", "r")


# 1. read one line at time : -

data3 = f.readline()
print("Read one line at time : ", data3)


# 2. read only specific letters of the file : - 

data2 = f.read(9)
print("Read specific amount of letter of the file : ", data2)   



