import pandas as pd

# Load the CSV file (Replace '2salary.csv' with the actual file path)
df = pd.read_csv('2salary.csv')

# Display the first few rows to check the data
print("First few rows of the dataset:\n", df.head())

# Assuming the salary column is named 'Salary'
if 'Salary' in df.columns:
    # Central Tendency Measures
    mean_salary = df['Salary'].mean()
    median_salary = df['Salary'].median()
    mode_salary = df['Salary'].mode()[0]  # Mode might return multiple values, so taking the first one

    # Dispersion Measures
    std_dev_salary = df['Salary'].std()
    variance_salary = df['Salary'].var()
    min_salary = df['Salary'].min()
    max_salary = df['Salary'].max()
    range_salary = max_salary - min_salary

    # Display Results
    print("\nCentral Tendency Measures:")
    print(f"Mean Salary: {mean_salary}")
    print(f"Median Salary: {median_salary}")
    print(f"Mode Salary: {mode_salary}")

    print("\nDispersion Measures:")
    print(f"Standard Deviation: {std_dev_salary}")
    print(f"Variance: {variance_salary}")
    print(f"Minimum Salary: {min_salary}")
    print(f"Maximum Salary: {max_salary}")
    print(f"Range: {range_salary}")

else:
    print("\nError: 'Salary' column not found in the dataset.")

