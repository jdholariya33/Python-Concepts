# Abstraction : - Hiding the implementation details of a class and only showing the essential features to the user.

class Student:
    def __init__(self):
        self.acc = False    # Accelerator
        self.brk = False    # Break
        self.clutch = False

    def start_car(self):
        self.clutch = True  # Unnecessary detail
        self.acc = True     # Unnecessary detail
        print("car Started...")
    
s1 = Student()
s1.start_car()  # necessary detail

