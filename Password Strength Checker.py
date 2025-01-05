import re
import nltk
from nltk.corpus import words
from nltk.data import find

# Download the word corpus if you haven't already
try:
    find('corpora/words.zip')
except:
    nltk.download('words')

# A list to store previously used passwords (for simplicity, we keep a small list here)
password_history = ["Password123!", "welcome2025", "12345678"]

# A list of common passwords for weak password check
common_passwords = ["123456", "password", "12345", "qwerty", "welcome", "admin"]

def check_password_strength(password):
    # Define strength criteria
    length_ok = len(password) >= 8 and len(password) <= 20
    upper_ok = bool(re.search(r'[A-Z]', password))
    lower_ok = bool(re.search(r'[a-z]', password))
    digit_ok = bool(re.search(r'[0-9]', password))
    special_char_ok = bool(re.search(r'[@#$%^&+=!]', password))

    # Check for common dictionary words (using nltk words corpus)
    if password.lower() in words.words():
        return "Weak password. It contains a common dictionary word."

    # Check if password is in the history (for simplicity, we are using a hardcoded list)
    if password in password_history:
        return "Weak password. It has been used recently."

    # Check for common passwords
    if password.lower() in common_passwords:
        return "Weak password. It is a common password."

    # Calculate the strength score
    score = 0
    if length_ok: score += 1
    if upper_ok: score += 1
    if lower_ok: score += 1
    if digit_ok: score += 1
    if special_char_ok: score += 1

    # Determine the strength based on score
    if score == 5:
        strength = "Strong"
    elif score == 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Generate feedback
    feedback = []
    if not length_ok:
        feedback.append("Password must be between 8 and 20 characters.")
    if not upper_ok:
        feedback.append("Password must contain at least one uppercase letter.")
    if not lower_ok:
        feedback.append("Password must contain at least one lowercase letter.")
    if not digit_ok:
        feedback.append("Password must contain at least one digit.")
    if not special_char_ok:
        feedback.append("Password must contain at least one special character.")
    
    return f"Password strength: {strength}\nSuggestions:\n" + "\n".join(feedback)


# Test the password checker
password = input("Enter your password: ")
print(check_password_strength(password))
