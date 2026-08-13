import random
import string   # A collection of string constants.

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

# Using For loop : Basic Method 

"""
password = ""
for i in range(pass_len):
    password += random.choice(charValues)
"""

# Using  list comprehension [Function for i in range(n)] : 

password = "".join([random.choice(charValues) for i in range(pass_len)])
# .join :- The string whose method is called is inserted in between each given string. The result is returned as a new string.
# eX :- '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
# EX :- '*'.join(['ab', 'pq', 'rs']) -> 'ab*pq*rs'

print("Your random password is:", password)