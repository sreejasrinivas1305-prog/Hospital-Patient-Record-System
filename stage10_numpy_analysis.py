# stage10_numpy_analysis.py
# Hospital Patient Record System - Week 10

import numpy as np

# Sample patient stay durations (in days)
stay_days = [3, 5, 2, 7, 4]

# Convert list to NumPy array
stay_array = np.array(stay_days)

# Calculations
total_stay = np.sum(stay_array)
average_stay = np.mean(stay_array)
max_stay = np.max(stay_array)
min_stay = np.min(stay_array)

print("=== Patient Stay Analysis ===")
print(f"Stay Days Data : {stay_array}")
print(f"Total Stay     : {total_stay} days")
print(f"Average Stay   : {average_stay:.2f} days")
print(f"Maximum Stay   : {max_stay} days")
print(f"Minimum Stay   : {min_stay} days")