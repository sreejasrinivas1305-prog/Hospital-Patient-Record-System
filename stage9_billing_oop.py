# stage9_billing_oop.py
# Hospital Patient Record System - Week 9

class HospitalEntity:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


class Billing(HospitalEntity):
    def __init__(self, patient_id, name, days, cost_per_day):
        super().__init__(patient_id, name)  # calling parent constructor
        self.days = days
        self.cost_per_day = cost_per_day

    def calculate_bill(self):
        return self.days * self.cost_per_day

    def display_bill(self):
        total = self.calculate_bill()
        print("\n--- Patient Bill ---")
        print(f"Patient ID: {self.patient_id}")
        print(f"Name      : {self.name}")
        print(f"Days      : {self.days}")
        print(f"Cost/Day  : {self.cost_per_day}")
        print(f"Total Bill: {total}")


# Main program
while True:
    print("\n=== Hospital Billing System ===")
    print("1. Generate Bill")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        days = int(input("Enter Number of Days: "))
        cost = int(input("Enter Cost per Day: "))

        bill = Billing(pid, name, days, cost)
        bill.display_bill()

    elif choice == "2":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")