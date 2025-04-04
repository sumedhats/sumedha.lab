import pandas as pd

# Replace 'your_file.csv' with the actual filename
file_path = 'your_file.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display last 3 rows
print("Last 3 rows of the DataFrame:")
print(df.tail(3))

# Display description of the DataFrame
print("\nDescription of the DataFrame:")
print(df.describe())

# Display info of the DataFrame
print("\nInfo about the DataFrame:")
df.info()

# Display column names
print("\nColumn names:")
print(df.columns.tolist())

