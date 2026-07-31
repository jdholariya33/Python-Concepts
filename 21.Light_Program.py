# Traffic Light Program

light = input("Enter the traffic light color (red, yellow, green): ").lower() # lower() method is used to convert the input to lowercase.

if light == "red":
    print("Stop! The light is red.")    
elif light == "yellow":
    print("Caution! The light is yellow. Prepare to stop.") 
elif light == "green":
    print("Go! The light is green.") 
else:
    print("Invalid input.") 