# Practice Question 5 :
# Que : - From a file containing numbers separated by comma,
#         print the count of even numbers.

# Method 1 : Basic Withour split method

with open("numbers.txt", "r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):     # Check "," for separate the number
            print(int(num))     # type  casting / passing
            num = ""
        else:
            num += data[i]

# method 2 : Using split method

count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
    
print(count)