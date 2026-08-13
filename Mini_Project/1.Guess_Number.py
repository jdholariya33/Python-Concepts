# 1. Guess the number game :

import random   # random Module :- Generate random num, char..

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target value or Quit : ")

    if userChoice == "Quit":
        break   

    userChoice = int(userChoice)
    if userChoice == target:
        print("Success : Correct Guess !")
        break
    elif userChoice > target:
        print("Your number was too big. guess a smaller number...")
    else:
        print("Your number was too small. guess a bigger number...")

print("_____Game_Over_____")
