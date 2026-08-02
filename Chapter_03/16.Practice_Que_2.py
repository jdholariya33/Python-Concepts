# Practical Question 2 :
# Question : - Write a program to check if a list contains a palindrome of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

# Method 1:

if list1 == list1.reverse():
    print(f"{list1} Contains a palindrome of elements")
else:
    print(f"{list1} Doesn't Contains a palindrome of elements")

if list2 == list2.reverse():
    print(f"{list2} Contains a palindrome of elements")
else:
    print(f"{list2} Doesn't Contains a palindrome of elements")


# Method 2:

list3 = list1.copy()
list4 = list2.copy()

list3.reverse()
list4.reverse()

if list1 == list3:
    print(f"{list1} Contains a palindrome of elements")
else:
    print(f"{list1} Doesn't Contains a palindrome of elements")

if list2 == list4:
    print(f"{list2} Contains a palindrome of elements")
else:
    print(f"{list2} Doesn't Contains a palindrome of elements")
