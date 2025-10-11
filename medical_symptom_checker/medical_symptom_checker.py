#!/usr/bin/env python3
"""
Medical Symptom Checker with Doctor Appointment Scheduler
A simple rule-based system to check symptoms and schedule appointments
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict

# Symptom database with possible conditions
SYMPTOM_DATABASE = {
    "fever": ["flu", "covid-19", "infection"],
    "cough": ["flu", "covid-19", "bronchitis", "allergy"],
    "headache": ["migraine", "tension headache", "flu"],
    "fatigue": ["flu", "anemia", "depression"],
    "sore throat": ["flu", "strep throat", "cold"],
    "nausea": ["food poisoning", "gastritis", "pregnancy"],
    "chest pain": ["heart condition", "anxiety", "muscle strain"],
    "shortness of breath": ["asthma", "covid-19", "anxiety"]
}

# Mock appointment slots
APPOINTMENTS = []

def check_symptoms(symptoms: List[str]) -> Dict[str, any]:
    """Analyze symptoms and suggest possible conditions"""
    symptoms = [s.lower().strip() for s in symptoms]
    possible_conditions = {}
    
    for symptom in symptoms:
        if symptom in SYMPTOM_DATABASE:
            for condition in SYMPTOM_DATABASE[symptom]:
                possible_conditions[condition] = possible_conditions.get(condition, 0) + 1
    
    # Sort by frequency
    sorted_conditions = sorted(possible_conditions.items(), key=lambda x: x[1], reverse=True)
    urgency = "high" if any(s in ["chest pain", "shortness of breath"] for s in symptoms) else "medium"
    
    return {
        "symptoms": symptoms,
        "possible_conditions": [c[0] for c in sorted_conditions[:3]],
        "urgency": urgency,
        "recommendation": "Consult a doctor immediately" if urgency == "high" else "Schedule an appointment"
    }

def schedule_appointment(patient_name: str, date: str, time: str, reason: str) -> Dict[str, any]:
    """Schedule a doctor appointment (simulated)"""
    try:
        appointment_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        
        if appointment_datetime < datetime.now():
            return {"success": False, "message": "Cannot schedule appointments in the past"}
        
        appointment = {
            "id": len(APPOINTMENTS) + 1,
            "patient_name": patient_name,
            "datetime": appointment_datetime.strftime("%Y-%m-%d %H:%M"),
            "reason": reason,
            "status": "scheduled"
        }
        
        APPOINTMENTS.append(appointment)
        return {"success": True, "message": "Appointment scheduled successfully", "appointment": appointment}
    except ValueError:
        return {"success": False, "message": "Invalid date/time format. Use YYYY-MM-DD HH:MM"}

def main():
    print("\n=== Medical Symptom Checker with Appointment Scheduler ===")
    print("\nAvailable symptoms to check:")
    print(", ".join(SYMPTOM_DATABASE.keys()))
    
    # Get symptoms
    symptom_input = input("\nEnter your symptoms (comma-separated): ")
    symptoms = [s.strip() for s in symptom_input.split(",")]
    
    # Analyze symptoms
    result = check_symptoms(symptoms)
    print(f"\n--- Analysis Results ---")
    print(f"Symptoms: {', '.join(result['symptoms'])}")
    print(f"Possible conditions: {', '.join(result['possible_conditions']) if result['possible_conditions'] else 'Unknown'}")
    print(f"Urgency: {result['urgency']}")
    print(f"Recommendation: {result['recommendation']}")
    
    # Schedule appointment
    schedule = input("\nWould you like to schedule an appointment? (yes/no): ").lower()
    if schedule == "yes":
        name = input("Enter your name: ")
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        print(f"Suggested date: {tomorrow} (or enter your preferred date)")
        date = input("Enter date (YYYY-MM-DD): ") or tomorrow
        time = input("Enter time (HH:MM, e.g., 14:30): ")
        reason = ", ".join(result['symptoms'])
        
        appointment_result = schedule_appointment(name, date, time, reason)
        print(f"\n{appointment_result['message']}")
        if appointment_result['success']:
            print(f"Appointment ID: {appointment_result['appointment']['id']}")
            print(f"Date & Time: {appointment_result['appointment']['datetime']}")

if __name__ == "__main__":
    main()
