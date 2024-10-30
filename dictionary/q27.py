#How do you nest dictionaries and access deeply nested values? 
store_inventory = {
    "electronics": {
        "laptops": {
            "MacBook": {"price": 1200, "stock": 5},
            "Dell": {"price": 800, "stock": 10}
        },
        "phones": {
            "iPhone": {"price": 1000, "stock": 15},
            "Samsung": {"price": 900, "stock": 20}
        }
    }
}

dell_price = store_inventory["electronics"]["laptops"]["Dell"]["price"]
print("Dell Laptop Price:", dell_price)  