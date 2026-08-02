# Practical Que 4 :
# Stores the tuple value of Question 3 in a list and sort them from "A" to "B"

grade = ("C", "D", "A", "A", "B", "B", "A")

list_grade = []
list_grade.append(grade)

print("grade tuple : " , grade)
print("List Grade", list_grade)

# But for easy method we create same value of list over here

grade_list = ["C", "D", "A", "A", "B", "B", "A"]

print("grade list : ", grade_list)
grade_list.sort()
print("Grade list in ascending order : ", grade_list)

