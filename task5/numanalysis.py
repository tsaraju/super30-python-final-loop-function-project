'''
5 Number Analysis Tool

Create a function that accepts a list and returns

largest number
smallest number
total
average
even count
odd count
positive count
negative count
Do not use min(), max(), or sum().
'''
def analyze_numbers(numbers):
    # Initialize values using the first number
    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    # Analyze each number
    for number in numbers:

        # Find largest number
        if number > largest:
            largest = number

        # Find smallest number
        if number < smallest:
            smallest = number

        # Calculate total
        total += number

        # Count even and odd numbers
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        # Count positive and negative numbers
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    # Calculate average
    average = total / len(numbers)

    return largest, smallest, total, average, even_count, odd_count, positive_count, negative_count


# Get numbers from the user
numbers = input("Enter numbers separated by spaces: ")

numbers = [int(number) for number in numbers.split()]

# Call the function
result = analyze_numbers(numbers)

# Display results
print("\n===== Number Analysis =====")
print("Largest number:", result[0])
print("Smallest number:", result[1])
print("Total:", result[2])
print("Average:", result[3])
print("Even count:", result[4])
print("Odd count:", result[5])
print("Positive count:", result[6])
print("Negative count:", result[7])

'''
Example Output
Enter numbers separated by spaces: 10 -5 20 7 -2 15 8

===== Number Analysis =====
Largest number: 20
Smallest number: -5
Total: 53
Average: 7.571428571428571
Even count: 4
Odd count: 3
Positive count: 5
Negative count: 2
'''