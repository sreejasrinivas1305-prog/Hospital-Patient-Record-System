# stage1_patient_input.py
# Hospital Patient Record System - Week 1

print("=== Hospital Patient Record System ===")

# Taking patient details
patient_id = input("Enter Patient ID: ")
name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
gender = input("Enter Patient Gender: ")

# Displaying patient details
print("\n--- Patient Details ---")
print(f"Patient ID   : {patient_id}")
print(f"Name         : {name}")
print(f"Age          : {age}")
print(f"Gender       : {gender}")
