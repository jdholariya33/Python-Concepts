# Nested-if Statement

age = int(input("Enter Your Age : "))
has_license = True

if age >= 18:
    if has_license:
        print("Eligible for driving a vehicle")
    else:
        print("Not Eligible for driving a vehicle")
else:
    print("You are Child..!")
