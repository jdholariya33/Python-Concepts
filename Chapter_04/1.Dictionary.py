# Dictionary : - Dictionaries are used to store data values in "key:value" pairs
#               They are "unordered, Mutable(Changeable)" and don't allow duplicate keys. 

# Syntax : - dictionary_name = {"Key1" : "Value", "Key2" : "Value"} 

info = {
    "name" : "Jay",
    "age" : 20,
    "college" : "Indus University",
    "skills" : ["Python", "Oops", "R", "Git"],
    "subjects" : ("DS", "OS", "DBMS", "Java"),
    "CGPA" : 9.45,
    "have_license" : True,
    19 : 35,
    19.33 : 33.77,
    True : False,
    ("set", "Dic") : 23
}

# Key   -->     we enter only immutable values like tuples, string, int, float as key not mutable like dictionary and list as key.

print("Information of the student : ", info)
print(type(info))

