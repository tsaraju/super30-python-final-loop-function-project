'''
11 Mini Authentication System

Create a small application supporting

predefined username/password
maximum login attempts
successful login
failed login
logout
retry logic

Use functions and loops appropriately.
'''
# Predefined username and password
USERNAME = "admin"
PASSWORD = "python123"


# Function to login
def login():
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin successful!")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts

            print("Invalid username or password.")

            if remaining > 0:
                print(f"Attempts remaining: {remaining}")
            else:
                print("Maximum login attempts reached.")

    return False


# Function to display the user menu
def user_menu():
    while True:
        print("\n===== User Menu =====")
        print("1. Welcome Message")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Welcome to the application, admin!")

        elif choice == "2":
            print("Logged out successfully.")
            return

        else:
            print("Invalid choice. Please try again.")


# Main function
def main():
    while True:
        print("\n===== Mini Authentication System =====")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if login():
                user_menu()
            else:
                print("Login failed.")

                retry = input("Do you want to try again? (yes/no): ").lower()

                if retry != "yes":
                    print("Thank you for using the application!")
                    break

        elif choice == "2":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the application
main()

'''
Example Outuput

===== Mini Authentication System =====
1. Login
2. Exit
Enter your choice: 1
Enter username: admin
Enter password: python123

Login successful!

===== User Menu =====
1. Welcome Message
2. Logout
Enter your choice: 
Invalid choice. Please try again.

===== User Menu =====
1. Welcome Message
2. Logout
Enter your choice: 1
Welcome to the application, admin!

===== User Menu =====
1. Welcome Message
2. Logout
Enter your choice: 2
Logged out successfully.

===== Mini Authentication System =====
1. Login
2. Exit
Enter your choice: 2
Thank you for using the application!

'''