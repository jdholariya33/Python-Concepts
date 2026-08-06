# Practical Question 2 :
# Que : - Write a function that replaces all occurrences of "python" with "Java" in above file.

def replace_word():

    with open("practice.txt", "r") as f:
        data = f.read()

    result = data.replace("python" , "java")
    print(result)

    with open("practice.txt", "w") as f:
        f.write(result)

replace_word()