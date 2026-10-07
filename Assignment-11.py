import pandas as pd
import numpy as np

# Create DataFrame
data = {
    "Name": ["Amit", "Rahul", None, "Sneha", "Priya",
             "Rohan", "Anjali", "Vikas", "Neha", None,
             "Karan", "Pooja", "Arjun", "Meena", "Raj"],

    "Age": [25, 32, 40, np.nan, 29,
            35, np.nan, 45, 28, 31,
            50, 27, 38, np.nan, 42],

    "Weight": [65, np.nan, 72, 58, 61,
               80, 55, np.nan, 68, 74,
               85, 60, np.nan, 63, 77],

    "Blood_Pressure": [120, 130, np.nan, 118, 125,
                       140, 110, 135, np.nan, 128,
                       145, 115, 132, 122, np.nan]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Weight"] = df["Weight"].fillna(df["Weight"].mean())
df["Blood_Pressure"] = df["Blood_Pressure"].fillna(
    df["Blood_Pressure"].mean()
)

# Drop rows where Name is missing
df = df.dropna(subset=["Name"])

print("\nAfter Mean Imputation and Removing Missing Names:")
print(df)