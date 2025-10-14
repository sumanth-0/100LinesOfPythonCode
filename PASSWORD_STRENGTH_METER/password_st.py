import re# Regular expressions for character checks

def evaluate_password_strength(password):
    score = 0
    feedback = []

    # --- Length Scoring ---
    length = len(password)
    if length < 6:
        feedback.append("Too short — at least 8 characters recommended.")
        score += 1
    elif 6 <= length < 8:
        feedback.append("Slightly short — try making it 8+ characters.")
        score += 3
    elif 8 <= length < 12:
        feedback.append("Good length.")
        score += 5
    else:
        feedback.append("Excellent length!")
        score += 7

    # --- Character Diversity ---
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 2
    else:
        feedback.append("Add special characters like @, #, $, etc.")

    # --- Bonus for Variety ---
    if (re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[^A-Za-z0-9]", password) and
        length >= 10):
        score += 1

    # --- Normalize Score (Max 10) ---
    score = min(score, 10)

    # --- Strength Label ---
    if score <= 3:
        strength = "Weak 😟"
    elif score <= 6:
        strength = "Moderate 😐"
    elif score <= 8:
        strength = "Strong 🙂"
    else:
        strength = "Very Strong 💪"

    # --- Display Results ---
    print(f"\nPassword: {'*' * len(password)}")
    print(f"Score: {score}/10 — {strength}")
    print("Feedback:")
    for tip in feedback:
        print(f" • {tip}")

# --- Run the Script ---
if __name__ == "__main__":
    user_pass = input("Enter your password: ")
    evaluate_password_strength(user_pass)
