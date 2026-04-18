# stage7_file_handling.py
# Hospital Patient Record System - Week 7

import csv

FILE_NAME = "patients.csv"


def save_patient(patient):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(patient)


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
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        gender = input("Enter Patient Gender: ")

        patient = [pid, name, age, gender]
        patients.append(patient)
        save_patient(patient)

        print("Patient saved successfully.")

    elif choice == "2":
        print("\n--- Patient Records ---")
        for p in patients:
            print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")

    elif choice == "3":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")