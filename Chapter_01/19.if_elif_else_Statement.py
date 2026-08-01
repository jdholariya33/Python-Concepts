# if-elif-else statement

marks = int(input("Enter your marks out of 100 : "))

if marks >= 90:
    print("A+ Grade")
elif 80 <= marks < 90:
    print("A Grade")
elif 70 <= marks < 80:
    print("B Grade")
elif 60 <= marks < 70:
    print("C Grade")
elif 50 <= marks < 60:
    print("D Grade")
elif 40 <= marks < 50:
    print("E Grade")
else:
    print("Better Luck Next Time..!")