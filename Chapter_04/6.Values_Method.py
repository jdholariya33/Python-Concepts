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

# 2. values() : - Returns all values of the dictionary

print("Product Values : ", product.values())    # Output : dict_values(['Laptop', 'HP', 45000, {'processor': 'Intel i5', 'ram': '16 GB', 'storage': '512 GB SSD'}, 'HP Pavilion'])
print("List Of the Values : ", list(product.values()))    # Output : ['Laptop', 'HP', 45000, {'processor': 'Intel i5', 'ram': '16 GB', 'storage': '512 GB SSD'}, 'HP Pavilion']


