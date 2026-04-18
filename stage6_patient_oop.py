# stage6_patient_oop.py
# Hospital Patient Record System - Week 6

class Patient:
    def __init__(self, pid, name, age, gender):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.ward = None

    def assign_ward(self, ward_name):
        self.ward = ward_name

    def display(self):
        print("\n--- Patient Details ---")
        print(f"ID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Ward: {self.ward}")


class Ward:
    def __init__(self, name):
        self.name = name
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        patient.assign_ward(self.name)

    def display_patients(self):
        print(f"\n--- Patients in {self.name} Ward ---")
        for p in self.patients:
            print(f"ID: {p.pid}, Name: {p.name}")


# Creating ward objects
general = Ward("General")
icu = Ward("ICU")
private = Ward("Private")

patients = []

while True:
    print("\n=== Hospital Patient Record System ===")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")
        ward_choice = input("Enter Ward (General/ICU/Private): ")

        patient = Patient(pid, name, age, gender)
        patients.append(patient)

        if ward_choice == "General":
            general.add_patient(patient)
        elif ward_choice == "ICU":
            icu.add_patient(patient)
        elif ward_choice == "Private":
            private.add_patient(patient)
        else:
            print("Invalid ward selected.")

        print("Patient added successfully.")

    elif choice == "2":
        for p in patients:
            p.display()

    elif choice == "3":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")