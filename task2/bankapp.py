'''
Banking Application

Create a menu-driven banking program supporting
Check balance
Deposit
Withdraw
Transaction history
Exit

Use functions for each operation and while for the application menu.
'''
# Function to check balance
def check_balance(balance):
    print(f"\nCurrent Balance: ₹{balance:.2f}")


# Function to deposit money
def deposit(balance, history):
    amount = float(input("Enter deposit amount: ₹"))

    if amount <= 0:
        print("Invalid deposit amount.")
    else:
        balance += amount
        history.append(f"Deposited ₹{amount:.2f}")
        print(f"₹{amount:.2f} deposited successfully.")

    return balance


# Function to withdraw money
def withdraw(balance, history):
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        history.append(f"Withdrawn ₹{amount:.2f}")
        print(f"₹{amount:.2f} withdrawn successfully.")

    return balance


# Function to display transaction history
def transaction_history(history):
    print("\n----- Transaction History -----")

    if len(history) == 0:
        print("No transactions yet.")
    else:
        for transaction in history:
            print(transaction)


# Main banking application
def main():
    balance = 0
    history = []

    while True:
        print("\n===== Banking Application =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            check_balance(balance)

        elif choice == "2":
            balance = deposit(balance, history)

        elif choice == "3":
            balance = withdraw(balance, history)

        elif choice == "4":
            transaction_history(history)

        elif choice == "5":
            print("Thank you for using the Banking Application!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the application
main()

'''
Example Output

===== Banking Application =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice (1-5): 2

Enter deposit amount: ₹5000
₹5000.00 deposited successfully.

===== Banking Application =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice (1-5): 3

Enter withdrawal amount: ₹1500
₹1500.00 withdrawn successfully.

===== Banking Application =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
Enter your choice (1-5): 4

----- Transaction History -----
Deposited ₹5000.00
Withdrawn ₹1500.00

'''