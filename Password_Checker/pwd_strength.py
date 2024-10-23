def password_strength(password):
    length = len(password)  # Calculate the length of the password
    has_upper = any(c.isupper() for c in password)  # Check for at least one uppercase letter
    has_digit = sum(c.isdigit() for c in password) > 2  # Check for more than 2 digits
    has_special = any(c in "!@#$%^&*()" for c in password)  # Check for at least one special character
    
    if password.isalnum():  # Check if the password only contains letters and digits
        suggestion = "Consider using a mix of letters, numbers, and symbols."
        return "Very Weak", suggestion  # Classify as Very Weak if only letters and digits
    if not has_upper and 6 <= length <= 7:  # Check for Weak password conditions
        suggestion = "Add an uppercase letter."
        return "Weak", suggestion
    if has_upper and has_digit and not has_special:  # Check for Good password conditions
        suggestion = "Add a special character."
        return "Good", suggestion
    if has_upper and has_digit and has_special and length >= 8:  # Strong password conditions
        return "Strong", "Your password is strong."
    
    return "Weak", "Consider meeting the criteria for a stronger password."  # Default case for weak passwords


password = input("Enter your password: ") 
strength, suggestion = password_strength(password) 
print(strength) 
print(suggestion) 

