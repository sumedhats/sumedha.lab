import pandas as pd

# Load the CSV file
df = pd.read_csv('2Salary.csv')

# Display the first few rows of the DataFrame
print("Data Preview:")
print(df.head())

# Assuming the salary column is named 'Salary'
salary_col = 'Salary'

if salary_col in df.columns:
    print(f"\nCentral Tendencies for '{salary_col}':")
    print(f"Mean: {df[salary_col].mean():.2f}")
    print(f"Median: {df[salary_col].median():.2f}")
    print(f"Mode: {df[salary_col].mode().tolist()}")

    print(f"\nDispersion Measures for '{salary_col}':")
    print(f"Standard Deviation: {df[salary_col].std():.2f}")
    print(f"Variance: {df[salary_col].var():.2f}")
    print(f"Range: {df[salary_col].max() - df[salary_col].min():.2f}")
    print(f"IQR (Interquartile Range): {df[salary_col].quantile(0.75) - df[salary_col].quantile(0.25):.2f}")
else:
    print(f"\nColumn '{salary_col}' not found in the dataset. Available columns: {df.columns.tolist()}")

