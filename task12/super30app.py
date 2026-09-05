'''
12 Super30 Python Utility Application

Create your own menu-driven application containing at least five utilities.

Examples

Calculator
Palindrome checker
Prime checker
Factorial calculator
Multiplication table
Number analyzer
Password checker

Students are encouraged to add their own features.
'''
# Super30 Python Utility Application

# 1. Calculator
def calculator():
    print("\n----- Calculator -----")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Result:", a + b)

    elif choice == "2":
        print("Result:", a - b)

    elif choice == "3":
        print("Result:", a * b)

    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", a / b)

    else:
        print("Invalid choice.")


# 2. Palindrome Checker
def palindrome_checker():
    text = input("\nEnter a word: ")

    if text.lower() == text.lower()[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


# 3. Prime Number Checker
def prime_checker():
    number = int(input("\nEnter a number: "))

    if number < 2:
        print("Not a prime number.")
        return

    for i in range(2, number):
        if number % i == 0:
            print("Not a prime number.")
            return

    print("It is a prime number.")


# 4. Factorial Calculator
def factorial_calculator():
    number = int(input("\nEnter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print(f"Factorial of {number} is {factorial}")


# 5. Multiplication Table
def multiplication_table():
    number = int(input("\nEnter a number: "))

    print(f"\n----- Table of {number} -----")

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


# 6. Number Analyzer
def number_analyzer():
    numbers = input("\nEnter numbers separated by spaces: ")

    numbers = [int(number) for number in numbers.split()]

    total = 0
    even_count = 0
    odd_count = 0

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        total += number

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    average = total / len(numbers)

    print("\n----- Number Analysis -----")
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Total:", total)
    print("Average:", average)
    print("Even count:", even_count)
    print("Odd count:", odd_count)


# 7. Password Checker
def password_checker():
    password = input("\nEnter your password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Strong password.")
    else:
        print("Weak password.")

        if len(password) < 8:
            print("- Password must contain at least 8 characters.")

        if not has_upper:
            print("- Add an uppercase letter.")

        if not has_lower:
            print("- Add a lowercase letter.")

        if not has_digit:
            print("- Add a number.")

        if not has_special:
            print("- Add a special character.")


# Main function
def main():

    while True:
        print("\n================================")
        print("   SUPER30 PYTHON UTILITIES")
        print("================================")
        print("1. Calculator")
        print("2. Palindrome Checker")
        print("3. Prime Number Checker")
        print("4. Factorial Calculator")
        print("5. Multiplication Table")
        print("6. Number Analyzer")
        print("7. Password Checker")
        print("8. Exit")
        print("================================")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            calculator()

        elif choice == "2":
            palindrome_checker()

        elif choice == "3":
            prime_checker()

        elif choice == "4":
            factorial_calculator()

        elif choice == "5":
            multiplication_table()

        elif choice == "6":
            number_analyzer()

        elif choice == "7":
            password_checker()

        elif choice == "8":
            print("\nThank you for using Super30 Python Utility Application!")
            break

        else:
            print("Invalid choice. Please select 1-8.")


# Start the application
main()

'''
Utilities included
Calculator → Addition, subtraction, multiplication, and division.
Palindrome Checker → Checks whether a word is a palindrome.
Prime Number Checker → Checks whether a number is prime.
Factorial Calculator → Calculates the factorial of a number.
Multiplication Table → Prints a table from 1 to 10.
Number Analyzer → Finds largest, smallest, total, average, even count, and odd count.
Password Checker → Checks password strength.
Exit → Closes the application.

Example Menu
================================
   SUPER30 PYTHON UTILITIES
================================
1. Calculator
2. Palindrome Checker
3. Prime Number Checker
4. Factorial Calculator
5. Multiplication Table
6. Number Analyzer
7. Password Checker
8. Exit
================================
Enter your choice (1-8):

'''