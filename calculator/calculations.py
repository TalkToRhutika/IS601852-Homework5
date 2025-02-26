"""
This module defines two classes: Calculation, which represents a single calculation operation, and Calculations, 
which manages a history of Calculation instances.
"""
from decimal import Decimal
from typing import Callable, List

# Define operation symbols outside the class
OPERATION_SYMBOLS = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/"
}

class Calculation:
    """Represents a single calculation operation."""
    def __init__(self, a: Decimal, b: Decimal, operation: Callable): 
        if not callable(operation):
            raise ValueError("Invalid operation provided.")
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """Performs the calculation."""
        if self.b is None:
            return self.operation(self.a)
        return self.operation(self.a, self.b)

    def update_operands(self, a: Decimal, b: Decimal):
        """Update the operands for the calculation."""
        self.a = a
        self.b = b

    @property
    def result(self) -> Decimal:
        """
        Return the result of the calculation.
        If b is None (for single-operand operations like square_root), only a is passed.
        """
        if self.b is None:
            return self.operation(self.a)
        return self.operation(self.a, self.b)

    def __str__(self):
        """Return a string representation of the calculation."""
        symbol = OPERATION_SYMBOLS.get(self.operation.__name__, "?")
        return f"{self.a} {symbol} {self.b} = {self.result}"


class Calculations:
    """Manages a collection of Calculation instances."""
    _history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls._history

    @classmethod
    def clear_history(cls) -> None:
        cls._history.clear()
