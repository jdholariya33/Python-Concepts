# Practical Question 2 :
# Que : - Write a recursive function to print all element in a list.
#         (Hint : - Use list & index as parameter.)

car = ["BMW M5","Audi A4", "Mercedes Benz", "Lamborghini Urus", "Nissan GTR", "Porsche 911", "Vellfire"]

def list_ele(list, idx):
    if idx == len(list):
        return 
    print(idx + 1, list[idx])
    return list_ele(list, idx + 1)

i = 0
print("Cars : ")
res = list_ele(car, i)
