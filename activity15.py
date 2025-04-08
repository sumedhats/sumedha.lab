import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
np.random.seed(42)
experience = np.round(np.random.normal(loc=5, scale=2, size=100), 1)  # Avg 5 years
experience = np.clip(experience, 0, None)  # No negative values
salary = 30000 + experience * 8000 + np.random.normal(0, 5000, 100)  # Add noise to salary

# Create DataFrame
sample_df = pd.DataFrame({
    "Experience (Years)": experience,
    "Salary": salary
})

# Plot the distribution of experience
plt.figure(figsize=(10, 6))
sns.histplot(sample_df["Experience (Years)"], bins=10, kde=True, color='skyblue')
plt.title("Distribution of Employee Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Number of Employees")
plt.grid(True)
plt.tight_layout()
plt.show()
