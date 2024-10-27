def format_email(template, user_info):
    """
    Fills in the placeholders in the email template with user-specific information.
    
    Parameters:
    - template (str): The email template with placeholders.
    - user_info (dict): A dictionary containing user-specific information.
    
    Returns:
    - str: The formatted email with user information.
    """
    for placeholder, value in user_info.items():
        template = template.replace(f"[{placeholder}]", value)
    return template

def main():
    # Sample email template
    email_template = """
    Dear [Name],

    I hope this message finds you well. I wanted to reach out regarding [Subject].

    Thank you for your attention to this matter.

    Best regards,
    [Your Name]
    """

    # User-specific information
    user_info = {
        'Name': input("Enter the recipient's name: "),
        'Subject': input("Enter the subject of the email: "),
        'Your Name': input("Enter your name: ")
    }

    # Generate and display the personalized email
    personalized_email = format_email(email_template, user_info)
    print("\n--- Personalized Email ---")
    print(personalized_email)

# Run the email formatter
if __name__ == "__main__":
    main()
