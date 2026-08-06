# Practice Que 4 :
# Que : - Write a function in which line of the file does the word "learning" occur first.
#         print -1 if word not found.

def find_word():
    with open("practice.txt", "r") as f:
        print("Searching Start...")
        for i in range(4):
            data = f.readline()
            i = 1
            if data.find("learning") != -1:
                print("learning found..!")
                print(i)
                break
            else:
                print("Finding...")
    return -1

find_word()
"""
def find_word_while():
    word = "learning"
    data = True # Data initialy True
    i = 1   # Line Number
    with open("practice.txt", "r") as f:
        while data: # if data empty than while loop close
            data = f.readline()
            if(word in data):
                print(i)
            i += 1
    return -1

find_word_while()
"""