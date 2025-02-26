"""
This module defines various mathematical operations, including addition, subtraction, multiplication, division, percentage, 
square root, and factorial, each implemented as a function that takes Decimal values as inputs and returns the result.
"""
from decimal import Decimal
import math

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == Decimal('0'):
        raise ValueError("An error occurred: Cannot divide by zero")  # Custom error message
    return a / b

def percentage(a: Decimal, b: Decimal) -> Decimal:
    return (a * b) / Decimal('100')

def square_root(a: Decimal) -> Decimal:
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return Decimal(math.sqrt(float(a)))

# def factorial(a: Decimal) -> Decimal:
#     if not a % 1 == 0:  # Check if the number is not an integer
#         raise ValueError("Factorial is only defined for integers.")
#     if a < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     return Decimal(math.factorial(int(a)))