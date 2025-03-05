"""Test cases for command functionality in the app."""

from decimal import Decimal
import pytest
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand
from app.plugins.percentage import PercentageCommand
from app.plugins.sqrt import SquareRootCommand

@pytest.mark.parametrize("operand1, operand2, command, expected", [  # Renamed "a" and "b" to "operand1" and "operand2"
    (Decimal('10'), Decimal('5'), AddCommand, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), SubtractCommand, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), MultiplyCommand, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), DivideCommand, Decimal('5')),  # Test division
    (Decimal('10.5'), Decimal('0.5'), AddCommand, Decimal('11.0')),  # Test addition with decimals
    (Decimal('10.5'), Decimal('0.5'), SubtractCommand, Decimal('10.0')),  # Test subtraction with decimals
    (Decimal('10.5'), Decimal('2'), MultiplyCommand, Decimal('21.0')),  # Test multiplication with decimals
    (Decimal('10'), Decimal('0.5'), DivideCommand, Decimal('20')),  # Test division with decimals
    (Decimal('50'), Decimal('10'), PercentageCommand, Decimal('5.0')),  # Test percentage
    (Decimal('25'), None, SquareRootCommand, Decimal('5.0')),  # Test square root
])

def test_calculation_commands(operand1, operand2, command, expected):  # Renamed "a" and "b" to "operand1" and "operand2"
    """
    Test calculation commands with various scenarios.

    This test ensures that the command class correctly performs the arithmetic operation
    (specified by the 'command' parameter) on two Decimal operands ('operand1' and 'operand2'),
    and that the result matches the expected outcome.

    Parameters:
        operand1 (Decimal): The first operand in the calculation.
        operand2 (Decimal): The second operand in the calculation (can be None for square root).
        command (function): The arithmetic command to perform.
        expected (Decimal): The expected result of the operation.
    """
    if operand2 is None:  # For square root, we only use one operand
        assert command().evaluate(operand1) == expected, f"Failed {command.__name__} command with {operand1}"
    else:
        assert command().evaluate(operand1, operand2) == expected, f"Failed {command.__name__} command with {operand1} and {operand2}"

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ZeroDivisionError
    """
    with pytest.raises(ZeroDivisionError, match="Cannot divide by 0!"):  # Expect a ZeroDivisionError to be raised.
        DivideCommand().evaluate(Decimal(3), Decimal(0))  # Attempt to perform the calculation, which should trigger the ZeroDivisionError.
