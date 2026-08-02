# Practice Question 1 :
# Que : - Write a program to ask the user to enter names of their 3 favorite movies and store them in a list.

a = input("Enter your 1st favourite movie : ")
b = input("Enter your 2nd favourite movie : ")
c = input("Enter your 3rd favourite movie : ")

# Method 1 : - Using list directly

movies = [a, b, c]
print("Your favorite movies are:", movies)

# Method 2 : - Using append() method

movie = []
movie.append(a)
movie.append(b)
movie.append(c)
print("Your favorite movies are:", movie)