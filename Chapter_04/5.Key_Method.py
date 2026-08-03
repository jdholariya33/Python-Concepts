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

print("Product Data : ", product)

# 1. key() : - Returns all keys of the dictionary

print("Product Keys : ", product.keys())    # Output : dict_keys(['name', 'brand', 'price', 'specifications', 'Model'])

print("List Of the Keys : ", list(product.keys()))    # Output : ['name', 'brand', 'price', 'specifications', 'Model'] 
# it converts the dict_keys object into a list.


