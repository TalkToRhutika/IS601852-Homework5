from decimal import Decimal
import decimal  # Importing the decimal module to handle InvalidOperation errors
import pytest
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize(
    "a, b, operation, expected_result", 
    [
        (1, 2, add, 3),  # Example: 1 + 2 = 3
        (5, 3, subtract, 2),  # Example: 5 - 3 = 2
        (4, 5, multiply, 20),  # Example: 4 * 5 = 20
        (20, 4, divide, 5),  # Example: 20 / 4 = 5
        (1, 0, divide, "An error occurred: Cannot divide by zero"),  # Division by zero
        (9, 3, 'unknown', "Unknown operation: unknown"),  # Invalid operation
        ('a', 3, add, "Invalid number input: a or 3 is not a valid number."),  # Invalid input test
        (5, 'b', subtract, "Invalid number input: 5 or b is not a valid number.")  # Invalid input test
    ]
)
def test_calculation_with_generated_data(a, b, operation, expected_result):
    try:
        num1, num2 = Decimal(a), Decimal(b)

        if operation == add:
            result = operation(num1, num2)
        elif operation == subtract:
            result = operation(num1, num2)
        elif operation == multiply:
            result = operation(num1, num2)
        elif operation == divide:
            if num2 == 0:
                result = "An error occurred: Cannot divide by zero"
            else:
                result = operation(num1, num2)
        else:
            result = f"Unknown operation: {operation}"

        assert result == expected_result

    except (ValueError, decimal.InvalidOperation):
        assert f"Invalid number input: {a} or {b} is not a valid number." == expected_result
