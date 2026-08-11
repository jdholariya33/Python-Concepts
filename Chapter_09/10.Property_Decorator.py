# Property Decorator : - We use @property decorator on any method in the class to use the method as a property.

# problem :- 
"""
class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem
        self.perc = str((self.phy + self.math + self.chem)/3) + "%"

s1 = Student(98, 97, 99)
print(s1.perc)  # Output :- 98.0%

s1.phy = 93
print(s1.phy)   # Output :- 93
print(s1.perc)  # Output :- 98.0% but percentage not change..because it calculate that fix values of marks
"""

"""
# Solution 1 :- (Simple)

class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    def calcPerc(self):
        self.perc = str((self.phy + self.math + self.chem)/3) + "%"
        print(self.perc)

s1 = Student(98, 97, 99)
s1.calcPerc()  # Output :- 98.0%

s1.phy = 93
print(s1.phy)   # Output :- 93
s1.calcPerc()  # Output :- 96.33333333333333%
"""

# Solution 2 : (use @property decorator)

class Student:
    def __init__(self, phy, math, chem):
        self.phy = phy
        self.math = math
        self.chem = chem

    #def calcPerc(self):
     #   self.perc = str((self.phy + self.math + self.chem)/3) + "%"
      #  print(self.perc)

    @property
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3) + "%"
    
s1 = Student(98, 97, 99)
print(s1.percentage)  # Output :- 98.0%

s1.phy = 93
print(s1.phy)   # Output :- 93
print(s1.percentage)  # Output :- 96.3333333333%