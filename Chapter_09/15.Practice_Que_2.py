# Practice Question 2 :
# Que : - Define a Employee class with attributes role, department and salary. This class also has showDetails() method.
#         Create an Engineer class that inherits properties from Employee and has additional attributes: name and age.

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role : ", self.role)
        print("Department : ", self.dept)
        print("salary : ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Accountant", "Finance", "60,000")

eng1 = Engineer("Prince", 26)
eng1.showDetails()
