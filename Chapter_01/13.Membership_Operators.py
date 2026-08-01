# 5. Membership Operators (in, not in)

fruits = ["Apple", "Banana", "Cheery"]  # List

print("Banana" in fruits)           # Output : - True 
print("banana" in fruits)           # Output : - False
print("Orange" in fruits)           # Output : - False
print("Cheery" not in fruits)       # Output : - False

text = "Python is open source language" # String

print("Python" in text)             # Output : - True
print("Python" not in text)         # Output : - False
print("language" in text)           # Output : - True

person = {"name" : "Jay" , "age" : 20}  # Dictionary

print("name" in person)               # Output : - True
print("Jay" in person)                # Output : - False (doesn't check value automatically)
print("Jay" in person.values())       # Output : - True


