# For both reading and writing : r+

f = open("Python/Chapter 7/sample.txt", "r+")   # r+ : - Overwrite the input at the starting of file.

f.write("This is sample file, just create for the coding and learning some new things.")

data = f.read()
print(data)     # Pointer (Cursor) Changed at the first text code

f.close()

