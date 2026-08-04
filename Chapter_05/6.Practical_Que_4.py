# Practical Question 4 :
# Que : - Print the elements of the following list using loop:
#         [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Method 1 :

i = 1 
list1 = []

while i <= 10:
    num = i * i     # same as i ** 2
    list1.append(num)
    i += 1

print("List : ", list1)


# Method 2 :

idx = 0
print("List : ")

# Traverse : visit and access every element in a data structure (such as a list, string, or dictionary) one by one in a specific order
list2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  

while idx < 10:
    print(list2[idx])   # list2[0], list2[1], list2[2]....
    idx += 1

