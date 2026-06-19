import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase password length to at least 12 characters.")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Strength Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, suggestions

password = input("Enter a password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for s in suggestions:
        print("-", s)
else:
    print("\nExcellent password!")