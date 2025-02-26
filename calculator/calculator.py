"""
Calculator module
"""
from typing import Callable, Union
from calculator.calculations import Calculation, Calculations
from calculator.operations import add, subtract, multiply, divide, percentage, square_root
from decimal import Decimal
import math

class Calculator:
    history = []

    @staticmethod
    def execute(a: Decimal, b: Union[Decimal, None], operation: Callable) -> Decimal:
        """Perform a calculation and store it in history."""
        if b is None:  # Handle single-operand functions (e.g. square_root)
            result = operation(a)
            calculation = Calculation(a, None, operation)
        else:
            result = operation(a, b)
            calculation = Calculation(a, b, operation)
        
        Calculations.add_calculation(calculation)  # Store in history
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, divide)

    @staticmethod
    def percentage(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.execute(a, b, percentage)

    @staticmethod
    def square_root(a: Decimal) -> Decimal:
        """Compute square root using execute() so it's stored in history."""
        return Calculator.execute(a, None, square_root)

    @staticmethod
    def clear_history():
        """Clear calculation history."""
        Calculator.history.clear()
        Calculations.clear_history()

    @staticmethod
    def get_last_calculation():
        """Retrieve the last calculation from history."""
        history = Calculations.get_history()
        if not history:
            print("DEBUG: No calculations in history!")
            return None
        return history[-1]

    def test_update_operands():
        calc = Calculation(Decimal(5), Decimal(3), add)
        calc.update_operands(Decimal(10), Decimal(5))
        assert calc.result == add(Decimal(10), Decimal(5))
