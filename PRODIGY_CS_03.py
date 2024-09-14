import re

def assess_password_strength(password):

    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))


    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])


    if strength_score == 5:
        feedback = "Very Strong: Your password is very strong!"
    elif strength_score == 4:
        feedback = "Strong: Your password is strong, but adding more characters can make it even better."
    elif strength_score == 3:
        feedback = "Moderate: Consider adding more variety (uppercase, digits, special characters) for a stronger password."
    elif strength_score == 2:
        feedback = "Weak: Your password needs more complexity (add uppercase, digits, special characters)."
    else:
        feedback = "Very Weak: Your password is too short or lacks variety. Add more characters and use a mix of different types."

    return feedback
password = input("Enter a password to assess: ")
print(assess_password_strength(password))
