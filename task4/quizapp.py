'''
4 Quiz Application

Create at least 5 Python questions.

The application should

display one question at a time
accept answers
check answers
maintain score
show final percentage
'''
# Function to display a question and get the answer
def ask_question(question, options, correct_answer):
    print("\n" + question)

    for option in options:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        print(f"The correct answer is {correct_answer}.")
        return 0


# Main function
def main():
    score = 0

    questions = [
        {
            "question": "1. Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. fun", "D. define"],
            "answer": "B"
        },
        {
            "question": "2. Which data type is used to store True or False?",
            "options": ["A. int", "B. str", "C. bool", "D. float"],
            "answer": "C"
        },
        {
            "question": "3. Which symbol is used for comments in Python?",
            "options": ["A. //", "B. /*", "C. #", "D. --"],
            "answer": "C"
        },
        {
            "question": "4. Which function is used to get input from the user?",
            "options": ["A. scan()", "B. input()", "C. get()", "D. read()"],
            "answer": "B"
        },
        {
            "question": "5. Which keyword is used to create a loop that continues while a condition is true?",
            "options": ["A. for", "B. loop", "C. repeat", "D. while"],
            "answer": "D"
        }
    ]

    # Display questions one at a time
    for q in questions:
        score += ask_question(
            q["question"],
            q["options"],
            q["answer"]
        )

    # Calculate percentage
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    # Display final result
    print("\n===== Quiz Result =====")
    print(f"Total Questions: {total_questions}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {total_questions - score}")
    print(f"Final Percentage: {percentage:.2f}%")


# Start the application
main()

'''
Example Output

1. Which keyword is used to define a function in Python?
A. function
B. def
C. fun
D. define
Enter your answer (A/B/C/D): B
Correct!

2. Which data type is used to store True or False?
A. int
B. str
C. bool
D. float
Enter your answer (A/B/C/D): C
Correct!

...

===== Quiz Result =====
Total Questions: 5
Correct Answers: 4
Wrong Answers: 1
Final Percentage: 80.00%

'''