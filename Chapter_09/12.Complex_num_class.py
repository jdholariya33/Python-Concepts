# Complex Number : - (3i + 4j) + (5i + 8j) = (8i + 12j)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +" , self.img, "j")

    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(3, 4)
num1.showNumber()

num2 = Complex(5, 8)
num2.showNumber()

# num3 = num1 + num2    --> Error : unsupported operand type(s) for +: 'Complex' and 'Complex'
num3 = num1.add(num2)
num3.showNumber()

