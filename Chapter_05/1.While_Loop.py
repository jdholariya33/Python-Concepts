# Loop : - Loops are used to repeat instruction.

# 1. While Loop : 

# Syntax : - while <condition>:
#            Code

count = 1   # Iterator

while count <= 5:   # Stoping Condtion..
    print("Hello, this is while loop..!")
    count = count + 1   # same as " count += 1
    # Completion of one cycle called one " Iteration "

print("Value of Count : ", count)


# Print From 1st to 10th value  --> Extraaa

i = 1

while i <= 10:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
    i += 1

print("Value of i : ", i)
