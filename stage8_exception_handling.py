# stage8_exception_handling.py
# Hospital Patient Record System - Week 8

import csv

FILE_NAME = "patients.csv"


def save_patient(patient):
    try:
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(patient)
    except Exception as e:
        print("Error saving data:", e)


def load_patients():
    patients = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                patients.append(row)
    except FileNotFoundError:
        print("File not found. Starting fresh.")
    return patients


patients = load_patients()

while True:
    print("\n=== Hospital Patient Record System ===")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))  # may cause error
            gender = input("Enter Patient Gender: ")

            patient = [pid, name, age, gender]
            patients.append(patient)
            save_patient(patient)

            print("Patient saved successfully.")

        except ValueError:
            print("Invalid input! Age must be a number.")

    elif choice == "2":
        try:
            print("\n--- Patient Records ---")
            for p in patients:
                print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")
        except Exception as e:
            print("Error displaying data:", e)

    elif choice == "3":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")