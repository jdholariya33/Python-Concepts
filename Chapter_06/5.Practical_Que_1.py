# Practical Question 1 :
# Que : - Write a function to print the length of a list. (list is the parameter)

cities = ["Mumbai", "Surat", "Ahemdabad", "Delhi", "Chennai"]
print("Cities : ", cities)

movies = ["HIT 3", "Nani's Paradise", "End game", "Spiderman", "Dacoit"]
print("Movies : ", movies)

def list_len(a):
    length = len(a)
    print("Length of given list : ", length)

list_len(cities)
list_len(movies) 

cities.append("Noida")
print(cities)

list_len(cities)
