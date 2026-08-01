# Single Line if / Ternary Operator

# 1. Syntax : - <var> = <Value1> if <Condition> else  <Value2>

food = input("Enter the food you want to eat : ").lower()
eat = "yes" if food == "pizza" else "no"
print(f"Do you want to eat pizza : {eat}")


# 2. Syntax : - <Statement1> if <Condition> else <Statement2>

food = input("Enter the food you want to eat : ").lower()
print("Sweet") if food == "cake" or food == "jalebi" else print("Not Sweet")

