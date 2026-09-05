'''
10 Expense Tracker

Allow a user to repeatedly enter

expense name
amount
Provide options to
add expense
view expenses
calculate total
find highest expense
exit
'''
# Function to add an expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: ₹"))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


# Function to view all expenses
def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
    else:
        print("\n----- Expense List -----")

        for expense in expenses:
            print(f"Name: {expense['name']}")
            print(f"Amount: ₹{expense['amount']:.2f}")
            print("------------------------")


# Function to calculate total expense
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Function to find the highest expense
def find_highest_expense(expenses):
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


# Main function
def main():
    expenses = []

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Find Highest Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total Expense: ₹{total:.2f}")

        elif choice == "4":
            highest = find_highest_expense(expenses)

            if highest is None:
                print("No expenses found.")
            else:
                print(f"Highest Expense: {highest['name']}")
                print(f"Amount: ₹{highest['amount']:.2f}")

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
main()

'''
Example Output

===== Expense Tracker =====
1. Add Expense
2. View Expenses
3. Calculate Total
4. Find Highest Expense
5. Exit

Enter your choice (1-5): 1
Enter expense name: Food
Enter expense amount: ₹500
Expense added successfully!

Enter your choice (1-5): 1
Enter expense name: Travel
Enter expense amount: ₹1200
Expense added successfully!

Enter your choice (1-5): 2

----- Expense List -----
Name: Food
Amount: ₹500.00
------------------------
Name: Travel
Amount: ₹1200.00
------------------------

Enter your choice (1-5): 3
Total Expense: ₹1700.00

Enter your choice (1-5): 4
Highest Expense: Travel
Amount: ₹1200.00

Enter your choice (1-5): 5
Thank you for using Expense Tracker!

'''