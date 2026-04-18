# stage11_pandas_analysis.py
# Hospital Patient Record System - Week 11

import pandas as pd

# Sample billing data
data = {
    "PatientID": ["P1", "P2", "P3", "P4"],
    "Ward": ["General", "ICU", "General", "Private"],
    "Cost": [2000, 5000, 3000, 7000]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=== Patient Billing Data ===")
print(df)

# Total cost
total_cost = df["Cost"].sum()

# Average cost
average_cost = df["Cost"].mean()

# Group by ward
ward_summary = df.groupby("Ward")["Cost"].sum()

print("\n--- Analysis ---")
print(f"Total Cost      : {total_cost}")
print(f"Average Cost    : {average_cost}")

print("\n--- Ward-wise Cost ---")
print(ward_summary)