'''
6 Employee Salary Analyzer

Given employee salaries, create functions to determine

total payroll
average salary
highest salary
lowest salary
employees earning above average
'''
# Function to calculate total payroll
def total_payroll(salaries):
    total = 0

    for salary in salaries:
        total += salary

    return total


# Function to calculate average salary
def average_salary(salaries):
    total = total_payroll(salaries)
    return total / len(salaries)


# Function to find highest salary
def highest_salary(salaries):
    highest = salaries[0]

    for salary in salaries:
        if salary > highest:
            highest = salary

    return highest


# Function to find lowest salary
def lowest_salary(salaries):
    lowest = salaries[0]

    for salary in salaries:
        if salary < lowest:
            lowest = salary

    return lowest


# Function to find employees earning above average
def above_average_employees(names, salaries, average):
    employees = []

    for i in range(len(salaries)):
        if salaries[i] > average:
            employees.append(names[i])

    return employees


# Main function
def main():
    names = []
    salaries = []

    number = int(input("Enter number of employees: "))

    # Accept employee details
    for i in range(number):
        name = input(f"\nEnter employee {i + 1} name: ")
        salary = float(input(f"Enter salary of {name}: ₹"))

        names.append(name)
        salaries.append(salary)

    # Calculate results
    total = total_payroll(salaries)
    average = average_salary(salaries)
    highest = highest_salary(salaries)
    lowest = lowest_salary(salaries)
    above_average = above_average_employees(names, salaries, average)

    # Display results
    print("\n===== Employee Salary Analysis =====")
    print(f"Total Payroll: ₹{total:.2f}")
    print(f"Average Salary: ₹{average:.2f}")
    print(f"Highest Salary: ₹{highest:.2f}")
    print(f"Lowest Salary: ₹{lowest:.2f}")

    print("\nEmployees earning above average:")

    for employee in above_average:
        print(employee)


# Start the program
main()

'''
Example Output

Enter number of employees: 5

Enter employee 1 name: Ravi
Enter salary of Ravi: ₹30000

Enter employee 2 name: Priya
Enter salary of Priya: ₹45000

Enter employee 3 name: Arun
Enter salary of Arun: ₹25000

Enter employee 4 name: Sneha
Enter salary of Sneha: ₹55000

Enter employee 5 name: Kiran
Enter salary of Kiran: ₹35000

===== Employee Salary Analysis =====
Total Payroll: ₹190000.00
Average Salary: ₹38000.00
Highest Salary: ₹55000.00
Lowest Salary: ₹25000.00

Employees earning above average:
Priya
Sneha

'''