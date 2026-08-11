# Practice Question 1 :
# Que : - Define a Circle class to create a circle with radius r using the constructor.
#         Define an Area() method of the class which calculates the area of the circle.
#         Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

pi = 22/7

class Circle:
    def __init__(self, r):
        self.r = r

    def Area(self):
        area =  pi * self.r * self.r    # Area = pi * r^2
        print("Area of the circle : ", area)

    def perimeter(self):
        perimeter = 2 * pi * self.r     # Perimeter = 2*pi*r 
        print("Perimeter of circle : ", perimeter)

c1 = Circle(21)
c1.Area()
c1.perimeter()

