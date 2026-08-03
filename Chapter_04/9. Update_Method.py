# Dictionary Methods : 

product = {
    "name" : "Laptop",
    "brand" : "HP",
    "price" : 45000,
    "specifications" : {
        "processor" : "Intel i5",
        "ram" : "16 GB",
        "storage" : "512 GB SSD"
    },
    "Model" : "HP Pavilion",
}

# 5. update(new_dict) : - Updates the dictionary with the specified key-value pairs.

print("Product Data Before Update : ", product)
product.update({"price" : 40000, "color" : "Silver"})
print("Product Data After Update : ", product)    # Output : {'name': 'Laptop', 'brand': 'HP', 'price': 40000, 'specifications': {'processor': 'Intel i5', 'ram': '16 GB', 'storage': '512 GB SSD'}, 'Model': 'HP Pavilion', 'color': 'Silver'}

