# For both reading and writing : a+

f = open("Python/Chapter 7/sample.txt", "a+")   # a+ : - Stream positioned at the end of the file.

f.write("This is sample file, just create for the coding and learning some new things.")

data = f.read()
print(data)     

f.close()

