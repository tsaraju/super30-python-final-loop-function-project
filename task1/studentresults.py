'''
Student Result Management System
Create functions to
accept student marks
calculate total
calculate percentage
assign grade
determine pass/fail
display result
Use loops wherever appropriate.
'''
# Function to accept student marks
def accept_marks():
    marks = []
    subjects = int(input("Enter number of subjects: "))

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    return marks


# Function to calculate total
def calculate_total(marks):
    total = 0

    for mark in marks:
        total += mark

    return total


# Function to calculate percentage
def calculate_percentage(total, number_of_subjects):
    percentage = total / number_of_subjects
    return percentage


# Function to assign grade
def assign_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "F"


# Function to determine pass/fail
def pass_fail(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"

    return "Pass"


# Function to display result
def display_result(marks, total, percentage, grade, result):
    print("\n----- Student Result -----")
    print("Marks:", marks)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)


# Main function
def main():
    marks = accept_marks()

    total = calculate_total(marks)

    percentage = calculate_percentage(total, len(marks))

    grade = assign_grade(percentage)

    result = pass_fail(marks)

    display_result(marks, total, percentage, grade, result)


# Start the program
main()

'''
Example Output
Enter number of subjects: 5
Enter marks for subject 1: 85
Enter marks for subject 2: 76
Enter marks for subject 3: 92
Enter marks for subject 4: 68
Enter marks for subject 5: 80

----- Student Result -----
Marks: [85.0, 76.0, 92.0, 68.0, 80.0]
Total: 401.0
Percentage: 80.2
Grade: B
Result: Pass
'''