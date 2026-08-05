# Practical Question 2 :
# Que : - Write a function to print elements of a list in a single line.(list is a parameter)

fruits = ["Apple", "Banana", "Cherry", "Dragon Friut", "Graves"]
cars = ["Audi", "BMW", "Creta", "Range Rover", "Jaguar"]

def print_list(list):
    for i in list:
        print(i, end = ", ")

print("List of Fruits : ", fruits)
print_list(fruits)

print("\nList of Cars : ", cars)
print_list(cars)

