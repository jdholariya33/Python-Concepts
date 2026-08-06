# With Syntax : -

# Syntax : - with open("file name", "mode") as var_name:    -->     as : - alias (Ironman is alias for Tony Stark)
#            data = var_name.read()


# Open with read mode

with open("D:\\VSCode\\Python\\Chapter 7\\demo.txt", "r") as f:   # with automatically closed the file
    data = f.read()
    print(data) 

# Open with write mode

with open("D:\\VSCode\\Python\\Chapter 7\\demo.txt", "w") as f:
    f.write("Hi Everyone, \nGood Morning")
    