# stage2_patient_validation.py
# Hospital Patient Record System - Week 2

print("=== Hospital Patient Record System ===")

patient_id = input("Enter Patient ID: ")
name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
gender = input("Enter Patient Gender (Male/Female): ")

# Validation
if name == "":
    print("Error: Name cannot be empty.")

elif age <= 0:
    print("Error: Age must be greater than zero.")

elif gender.lower() != "male" and gender.lower() != "female":
    print("Error: Gender must be Male or Female.")

else:
    print("\n--- Patient Details (Validated) ---")
    print(f"Patient ID   : {patient_id}")
    print(f"Name         : {name}")
    print(f"Age          : {age}")
    print(f"Gender       : {gender}")
