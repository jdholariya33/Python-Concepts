# String Functions

str = "i am a student."

# 1. endswith(substr)    -->     Returns true if string ends with substr

print(str.endswith("nt."))  # Output : - True
print(str.endswith("ok"))  # Output : - False

# 2. capitalize()   -->     Capitalizes first char

print(str.capitalize()) # Output : - I am a student.

# 3. replace(old , new)     -->     Replaces all occurrences of old value with new

print(str.replace("a" , "A"))   # Output : - i Am A student.
print(str.replace("student." , "coder."))   # Output : - i am a coder.

# 4. find(word)     -->     return 1st index of 1st occurrer

print(str.find("a"))    # Output : - 2
print(str.find("student.")) # Output : - 7
print(str.find("coder"))    # Output : - -1

# 5. count(substr)  -->     Counts the occurrence of sub string

print(str.count("a"))   # Output : - 2
print(str.count("stu")) # Output : - 1