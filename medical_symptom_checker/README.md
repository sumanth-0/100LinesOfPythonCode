# Medical Symptom Checker with Doctor Appointment Scheduler

## Description
A simple Python script that helps users check their medical symptoms and schedule doctor appointments. This implementation uses a rule-based system to analyze symptoms and provide recommendations.

## Features
- **Symptom Analysis**: Analyzes user-reported symptoms against a predefined database
- **Condition Prediction**: Suggests possible medical conditions based on symptom patterns
- **Urgency Assessment**: Determines whether symptoms require immediate attention
- **Appointment Scheduling**: Simulated doctor appointment booking system
- **User-Friendly CLI**: Interactive command-line interface for easy interaction

## How It Works

### Symptom Database
The script maintains a symptom database mapping common symptoms to potential conditions:
- Fever → Flu, COVID-19, Infection
- Cough → Flu, COVID-19, Bronchitis, Allergy
- Headache → Migraine, Tension Headache, Flu
- And more...

### Usage
1. Run the script: `python medical_symptom_checker.py`
2. Enter your symptoms (comma-separated)
3. Review the analysis results:
   - Identified symptoms
   - Possible conditions
   - Urgency level
   - Recommendations
4. Optionally schedule an appointment

## Example

```
=== Medical Symptom Checker with Appointment Scheduler ===

Available symptoms to check:
fever, cough, headache, fatigue, sore throat, nausea, chest pain, shortness of breath

Enter your symptoms (comma-separated): fever, cough, fatigue

--- Analysis Results ---
Symptoms: fever, cough, fatigue
Possible conditions: flu, covid-19
Urgency: medium
Recommendation: Schedule an appointment

Would you like to schedule an appointment? (yes/no): yes
Enter your name: John Doe
Suggested date: 2025-10-12 (or enter your preferred date)
Enter date (YYYY-MM-DD): 2025-10-12
Enter time (HH:MM, e.g., 14:30): 14:30

Appointment scheduled successfully
Appointment ID: 1
Date & Time: 2025-10-12 14:30
```

## Requirements
- Python 3.x
- No external libraries required (uses only standard library)

## Note
This is a simulated system for educational purposes. It is **not** a replacement for professional medical advice. Always consult with a qualified healthcare provider for medical concerns.

## Implementation Details
- Rule-based symptom matching
- In-memory appointment storage (simulated)
- Date/time validation for appointments
- Under 100 lines of Python code as per repository guidelines
