# 5. sort() : - This method is used to sort the elements of the list in ascending order.

list = [20, 70, 10, 50, 30, 40] # List of integers

print("List before sort : ", list)
list.sort() # Sorting the list in ascending order   -->     same as list.sort(reverse=False)
print("List after sort in ascending order : ", list)

list.sort(reverse=True) # Sorting the list in descending order
print("List after sort in descending order : ", list)


print("List after sort in ascending order : ", list.sort())
print(list)
print("List after sort in descending order : ", list.sort(reverse=True))
print(list)

fruits = ['banana', 'apple', 'mango', 'grapes', 'orange'] # List of strings

print("List of fruits before sort : ", fruits)
fruits.sort() # Sorting the list of strings in ascending order
print("List of fruits after sort in ascending order : ", fruits)