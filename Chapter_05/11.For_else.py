# For with else : -

num = [1, 3, 5, 7, 9]

for el in num:
    print(el)
else:       # optional  -->     Mainly it use when we use break keyword in loop.
    print("End of loop..")

for el in num:
    if(el == 3):
        print("3 Found")
        break
    print(el)
else:
    print("End of the entire loop") # It only work (print) when whole loop will complete.