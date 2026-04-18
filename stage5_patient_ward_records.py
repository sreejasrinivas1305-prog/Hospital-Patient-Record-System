# stage5_patient_ward_records.py
# Hospital Patient Record System - Week 5

patients = []
wards = {
    "General": [],
    "ICU": [],
    "Private": []
}


def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Patient Gender: ")
    ward = input("Enter Ward (General/ICU/Private): ")

    if ward not in wards:
        print("Invalid ward selected.")
        return

    patient = {
        "id": pid,
        "name": name,
        "age": age,
        "gender": gender,
        "ward": ward
    }

    patients.append(patient)
    wards[ward].append(patient)

    print("Patient added successfully.")


def display_patients():
    print("\n--- All Patients ---")
    for p in patients:
        print(f"ID: {p['id']}, Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}, Ward: {p['ward']}")


def display_ward_patients():
    ward = input("Enter Ward to display (General/ICU/Private): ")

    if ward in wards:
        print(f"\n--- Patients in {ward} Ward ---")
        for p in wards[ward]:
            print(f"ID: {p['id']}, Name: {p['name']}")
    else:
        print("Invalid ward.")


while True:
    print("\n=== Hospital Patient Record System ===")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Display Ward-wise Patients")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        display_patients()
    elif choice == "3":
        display_ward_patients()
    elif choice == "4":
        print("Exiting system.")
        break
    else:
        print("Invalid choice.")
