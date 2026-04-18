# stage12_visualization.py
# Hospital Patient Record System - Week 12

import matplotlib.pyplot as plt

# Sample data
wards = ["General", "ICU", "Private"]
patients = [10, 5, 7]
costs = [2000, 5000, 7000]

# Bar Chart (Ward-wise patient count)
plt.figure()
plt.bar(wards, patients)
plt.title("Ward-wise Patient Count")
plt.xlabel("Ward")
plt.ylabel("Number of Patients")
plt.show()

# Line Graph (Cost trend)
plt.figure()
plt.plot(wards, costs, marker='o')
plt.title("Ward-wise Cost Trend")
plt.xlabel("Ward")
plt.ylabel("Cost")
plt.show()

# Pie Chart (Patient distribution)
plt.figure()
plt.pie(patients, labels=wards, autopct='%1.1f%%')
plt.title("Patient Distribution by Ward")
plt.show()