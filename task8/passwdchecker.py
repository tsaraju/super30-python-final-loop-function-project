'''
8 Password Strength Checker

Create a function that checks whether a password contains

uppercase
lowercase
number
special character
minimum 8 characters

Return a meaningful strength/result.
'''
# Function to check password strength
def check_password(password):
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    # Check each character
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True
        else:
            has_special = True

    # Check minimum length
    has_min_length = len(password) >= 8

    # Display missing requirements
    if not has_min_length:
        print("Password must contain at least 8 characters.")

    if not has_uppercase:
        print("Password must contain an uppercase letter.")

    if not has_lowercase:
        print("Password must contain a lowercase letter.")

    if not has_number:
        print("Password must contain a number.")

    if not has_special:
        print("Password must contain a special character.")

    # Determine strength
    if (has_min_length and has_uppercase and has_lowercase
            and has_number and has_special):
        return "Strong Password"
    else:
        return "Weak Password"


# Get password from user
password = input("Enter your password: ")

# Check password
result = check_password(password)

print("\nResult:", result)

'''
Example outputs

Enter your password: Python@123

Result: Strong Password

Enter your password: python123

Password must contain an uppercase letter.
Password must contain a special character.

Result: Weak Password


'''