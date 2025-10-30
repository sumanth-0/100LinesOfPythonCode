# hospital_tracker.py

import csv
import pandas as pd
import numpy as np


class Patient:
    def __init__(self, name, age, symptoms, doctor, department):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.doctor = doctor
        self.department = department

    def is_critical(self): 
        return 'chest pain' in self.symptoms.lower() or 'breathing' in self.symptoms.lower()

    def display(self):  # ✅ Topic 1: Display Patient Info
        print("\n--- Patient Information ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Symptoms: {self.symptoms}")
        print(f"Doctor: {self.doctor}")
        print(f"Department: {self.department}")
        print(f"Condition: {'Critical' if self.is_critical() else 'Stable'}")

# ✅ Inheritance and Polymorphism
class EmergencyPatient(Patient):
    def __init__(self, name, age, symptoms, doctor, department, ambulance):
        super().__init__(name, age, symptoms, doctor, department)
        self.ambulance = ambulance

    def display(self):  # ✅ Polymorphism
        super().display()
        print(f"Ambulance Arrival: {self.ambulance}")

# ✅ Topic 8: File Handling - Save patient to CSV
def save_patient_to_file(patient, filename='patients.csv'):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            patient.name,
            patient.age,
            patient.symptoms,
            patient.doctor,
            patient.department,
            'Yes' if patient.is_critical() else 'No'
        ])

# ✅ Topic 9: Pandas and NumPy for data analysis
def analyze_data(filename='patients.csv'):
    try:
        df = pd.read_csv(filename, header=None)
        df.columns = ['Name', 'Age', 'Symptoms', 'Doctor', 'Department', 'Critical']
        print("\n--- Patient Data Summary ---")
        print(df)

        print("\n--- Patients per Department ---")
        print(df['Department'].value_counts())

        print("\n--- Critical vs Stable Patients ---")
        print(df['Critical'].value_counts())

        print("\n--- Average Age of Patients ---")
        print(np.mean(df['Age']))

    except FileNotFoundError:
        print("No data available yet. Add some patients first.")

# ✅ Data Structures
patients_list = []   # ✅ List
patient_rolls = set()  # ✅ Set to avoid duplicates

# ✅ Topic 3, 4: Loops and Functions - Menu System
def main():
    while True:
        print("\n========== Hospital Patient Tracker ==========")
        print("1. Add New Patient")
        print("2. Display All Patients")
        print("3. Analyze Patient Data")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter patient name: ")
            if name in patient_rolls:
                print("Patient already exists.")
                continue
            age = int(input("Enter age: "))
            symptoms = input("Enter symptoms: ")
            doctor = input("Enter doctor name: ")
            department = input("Enter department: ")
            ambulance = input("Arrived by ambulance? (yes/no): ").lower()

            if ambulance == 'yes':
                p = EmergencyPatient(name, age, symptoms, doctor, department, ambulance)
            else:
                p = Patient(name, age, symptoms, doctor, department)

            patients_list.append(p)
            patient_rolls.add(name)
            save_patient_to_file(p)
            print("✅ Patient record added successfully.")

        elif choice == '2':
            if not patients_list:
                print("No patient records to display.")
            for p in patients_list:
                p.display()

        elif choice == '3':
            analyze_data()

        elif choice == '4':
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

# Run the program
main()
