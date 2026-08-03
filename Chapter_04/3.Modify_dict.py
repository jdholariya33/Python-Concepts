# Modify Dictionary :

info = {
    "name" : "meet",
    "age" : 20,
    "CGPA" : 7.58,
    "marks" : [78, 81, 70, 75, 88],
    "Male" : True
}

print("Information of the person : ", info)

info["name"] = "Krish"  # Change the value of name (key)
info["surname"] = "Sangani"   # Add new key : value pair
info["Male"] = ""   # remove value of Male (key) or change with empty string

print("After modification : ", info)

# Empty dictionary

empty_dict = {}

print("Empty Dictionary : ", empty_dict)
print("Type : ", type(empty_dict))

empty_dict["name"] = "Krisha"
print(empty_dict)