# Practice Question 4 : 
# Que : - Search if the word "Learning" exists in the file or not.

with open("practice.txt", "r") as f:
    data = f.read()

print(data)

result = data.find("learning")

if result != -1:
    print("learning found..!")
else:
    print("learning doesn't found..!")
