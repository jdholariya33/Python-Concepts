# Practice Program
# Print Output For : -
# A = 5 & G = M     -->     Ans :- Fee is 300
# A = 2 & G = F     -->     Ans :- Fee is 200

A = int(input("Enter the value of A: "))
G = input("Enter the gender (M/F): ").upper()

if (A == 1 or A == 2) and G == "M":
    print("Fee is 100")
elif(A == 3 or A == 4 or G == "F"):
    print("Fee is 200")
elif(A == 5 and G == "M"):
    print("Fee is 300") 
else:
    print("No Fee")



