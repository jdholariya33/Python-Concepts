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

# 4. get("<key>") : - Returns the value of the specified key. If the key does not exist, it returns None (or a default value if provided).

print("Product Name : ", product["name"])    # Output : Laptop

print("Product Name : ", product.get("name"))    # Output : Laptop
print("Product Color : ", product.get("color"))    # Output : None


