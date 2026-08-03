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

# 3. items() : - Returns all key-value pairs of the dictionary as tuples

print("Product Items : ", product.items())    # Output : dict_items([('name', 'Laptop'), ('brand', 'HP'), ('price', 45000), ('specifications', {'processor': 'Intel i5', 'ram': '16 GB', 'storage': '512 GB SSD'}), ('Model', 'HP Pavilion')])
print("List Of the Items : ", list(product.items()))    # Output : [('name', 'Laptop'), ('brand', 'HP'), ('price', 45000), ('specifications', {'processor': 'Intel i5', 'ram': '16 GB', 'storage': '512 GB SSD'}), ('Model', 'HP Pavilion')]

pairs = list(product.items())
print("First Pair : ", pairs[0])    # Output : ('name', 'Laptop')


