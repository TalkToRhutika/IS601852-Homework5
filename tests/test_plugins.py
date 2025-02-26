import pytest
from app.plugins.multiply import MultiplyCommand
from app.plugins.percentage import PercentageCommand
from app.plugins.sqrt import SquareRootCommand

def test_multiply_command_invalid_input(capfd):
    command = MultiplyCommand()
    command.execute("abc", "3")

    captured = capfd.readouterr()
    assert "Error: Invalid numbers. Please provide valid numeric inputs." in captured.out  # ✅ Match test output

def test_percentage_command_invalid(capfd):
    command = PercentageCommand()
    command.execute("xyz", "10")

    captured = capfd.readouterr()
    assert "Error: Invalid input. Please provide valid numbers." in captured.out  # ✅ Match test output

def test_sqrt_command_invalid(capfd):
    command = SquareRootCommand()
    command.execute("-9")

    captured = capfd.readouterr()
    assert "Error: Cannot calculate square root of a negative number." in captured.out  # ✅ Match test output

def test_percentage_command(capfd):
    command = PercentageCommand()
    command.execute("200", "10")

    captured = capfd.readouterr()
    assert "The result of 10% of 200 is 20" in captured.out  # ✅ Match test output

def test_sqrt_command(capfd):
    command = SquareRootCommand()
    command.execute("16")

    captured = capfd.readouterr()
    assert "The square root of 16 is 4.00" in captured.out  # ✅ Match test output
