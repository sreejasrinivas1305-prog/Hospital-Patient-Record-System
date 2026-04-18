# stage3_patient_search.py
# Hospital Patient Record System - Week 3

patients = []  # list to store patient records

while True:
    print("\n=== Hospital Patient Record System ===")
    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient by ID")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")

        patient = [pid, name, age, gender]
        patients.append(patient)

        print("Patient added successfully.")

    elif choice == "2":
        print("\n--- Patient List ---")
        for p in patients:
            print(f"ID: {p[0]}, Name: {p[1]}, Age: {p[2]}, Gender: {p[3]}")

    elif choice == "3":
        search_id = input("Enter Patient ID to search: ")
        found = False

        for p in patients:
            if p[0] == search_id:
                print("\nPatient Found:")
                print(f"ID: {p[0]}")
                print(f"Name: {p[1]}")
                print(f"Age: {p[2]}")
                print(f"Gender: {p[3]}")
                found = True
                break

        if not found:
            print("Patient not found.")

    elif choice == "4":
        print("Exiting system.")
        break

    else:
        print("Invalid choice. Please try again.")
