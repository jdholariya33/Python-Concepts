# Nested Dictionary :

student = {
    "name" : "Rahul",
    "subject" : {
        "phy" : 87,
        "math" : 93,
        "chem" : 80,
        "comp" : 91
    },
    "age" : 18,
    "city" : "Delhi"
}

print("Student Data : ", student)

print("Student's Marks : ", student["subject"])
print("Student's physics marks : ", student["subject"]["phy"])

student["subject"]["hindi"] = 83

print("Student New Data : ", student["subject"])

