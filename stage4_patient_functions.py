# stage4_patient_functions.py
# Hospital Patient Record System - Week 4

patients = []


def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    patients.append([pid, name, age, gender])
    print("Patient added successfully.")


def display_patients():
    print("\n--- Patient List ---")
    for p in patients:
        print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")


def search_patient():
    search_id = input("Enter Patient ID to search: ")
    for p in patients:
        if p[0] == search_id:
            print("\nPatient Found:")
            print(f"ID: {p[0]}")
            print(f"Name: {p[1]}")
            print(f"Age: {p[2]}")
            print(f"Gender: {p[3]}")
            return
    print("Patient not found.")


def delete_patient():
    del_id = input("Enter Patient ID to delete: ")
    for p in patients:
        if p[0] == del_id:
            patients.remove(p)
            print("Patient deleted successfully.")
            return
    print("Patient not found.")


while True:
    print("\n=== Hospital Patient Record System ===")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        search_patient()
    elif choice == "4":
        delete_patient()
    elif choice == "5":
        print("Exiting system.")
        break
    else:
        print("Invalid choice.")
