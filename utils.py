# utils.py
"""
A collection of utility functions for common tasks. 
These functions are designed to be simple and useful for new Python learners.
"""

# Function 1: Calculate the factorial of a number
def factorial(n):
    """
    Returns the factorial of a given number n.
    Factorial of 5 (5!) = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Function 2: Check if a string is a palindrome
def is_palindrome(s):
    """
    Returns True if the input string is a palindrome, False otherwise.
    A palindrome is a word that reads the same forwards and backwards, e.g., 'radar' or 'madam'.
    """
    s = s.lower().replace(' ', '')  # Normalize the string (case-insensitive, no spaces)
    return s == s[::-1]


# Function 3: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32
    """
    return (celsius * 9/5) + 32


# Function 4: Generate a list of prime numbers up to a given number
def generate_primes(limit):
    """
    Returns a list of all prime numbers up to the specified limit.
    """
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


# Function 5: Read a file and return its content as a string
def read_file(file_path):
    """
    Reads the content of a file and returns it as a string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."


# Function 6: Calculate the average of a list of numbers
def calculate_average(numbers):
    """
    Returns the average (mean) of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


# Function 7: Capitalize the first letter of each word in a string
def capitalize_words(sentence):
    """
    Capitalizes the first letter of every word in the input sentence.
    """
    return ' '.join([word.capitalize() for word in sentence.split()])
