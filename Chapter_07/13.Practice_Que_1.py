# Practical Question 1 : 
# Que : - Create a new file "practice.txt" using python. Add the following data in it.
"""
            Hi everyone
            we are learning I/O 
            using python.
            I like proogramming in python.
"""

f = open("practice.txt" , "w")

f.write("Hi everyone\nwe are learning I/O\nusing python.\nI like proogramming in python.")

f.close()