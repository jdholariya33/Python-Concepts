# Practice Question 1 :
# Que : - Create student class that takes name and marks of 3 subjects as arguments in constructor.
#         Then create a method to print the average.

class Student:
    def __init__(self, name, marks):    # Using List 
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi, {self.name} Your average score is : {sum/3}")

s1 = Student("Jay", [89, 92, 97])
s1.avg()

class Student:
    def __init__(self, name, phy, chem, math):  # Using basic method
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    def avg(self):
        avg = (self.phy + self.chem + self.math)/3
        print("Average of three numbers : ", avg)

s1 = Student("Jay", 89, 92, 97)
s1.avg()
