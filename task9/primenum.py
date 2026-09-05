''' 
9 Prime Number Analyzer

Take two numbers representing a range.

Create functions to
find prime numbers
count primes
calculate their sum

display the largest prime found
'''
# Function to check whether a number is prime
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


# Function to find prime numbers in a range
def find_primes(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


# Function to count primes
def count_primes(primes):
    return len(primes)


# Function to calculate sum of primes
def sum_primes(primes):
    total = 0

    for prime in primes:
        total += prime

    return total


# Function to find the largest prime
def largest_prime(primes):
    if len(primes) == 0:
        return None

    largest = primes[0]

    for prime in primes:
        if prime > largest:
            largest = prime

    return largest


# Main function
def main():
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    primes = find_primes(start, end)

    print("\n===== Prime Number Analysis =====")

    if len(primes) == 0:
        print("No prime numbers found in the given range.")
    else:
        print("Prime numbers:", primes)
        print("Number of primes:", count_primes(primes))
        print("Sum of primes:", sum_primes(primes))
        print("Largest prime:", largest_prime(primes))


# Start the program
main()

'''
Example Output
Enter starting number: 10
Enter ending number: 30

===== Prime Number Analysis =====
Prime numbers: [11, 13, 17, 19, 23, 29]
Number of primes: 6
Sum of primes: 112
Largest prime: 29

'''