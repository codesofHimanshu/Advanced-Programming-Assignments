# Assignment 4: Product Stock Checker

# List of products (each product is stored as a dictionary)
products = [
    {"name": "Laptop", "stock": 15},
    {"name": "Mouse", "stock": 5},
    {"name": "Keyboard", "stock": 8},
    {"name": "Monitor", "stock": 12},
    {"name": "USB Cable", "stock": 3}
]

print("Products with stock less than 10:\n")

# Loop through products and check stock
for product in products:
    if product["stock"] < 10:
        print(product["name"], "- Stock:", product["stock"])
