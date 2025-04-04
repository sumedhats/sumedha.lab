import pandas as pd

# List of dictionaries representing products
products = [
    {"Name": "Laptop", "Category": "Electronics", "Price": 50000},
    {"Name": "Phone", "Category": "Electronics", "Price": 20000},
    {"Name": "Shoes", "Category": "Fashion", "Price": 3000},
    {"Name": "Watch", "Category": "Accessories", "Price": 1500},
]

# Create DataFrame
df = pd.DataFrame(products)

# Add a new column for Discounted Price (10% discount)
df["Discounted Price"] = df["Price"] * 0.9

# Display the DataFrame
print(df)

