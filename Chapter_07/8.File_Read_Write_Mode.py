# For both reading and writing : w+

f = open("Python/Chapter 7/sample.txt", "w+")   # w+ : - truncated

f.write("This is sample file, just create for the coding and learning some new things.")

data = f.read()
print(data)     

f.close()

