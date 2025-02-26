import pytest
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.calculations import Calculation, Calculations
from calculator.operations import add, subtract, multiply, divide, square_root

def test_calculator_init():
    """Test that Calculator initializes without error."""
    calc = Calculator()
    assert calc  # ✅ Confirm instance creation

@pytest.fixture
def setup_calculations():
    """Setup calculations."""
    calc = Calculation(Decimal(2), Decimal(3), add)
    Calculations.add_calculation(calc)
    yield calc
    Calculations.clear_history()

def test_setup_calculations_fixture(setup_calculations):
    """Ensure the setup_calculations fixture creates a valid calculation."""
    assert isinstance(setup_calculations, Calculation)
    assert setup_calculations.result == add(Decimal(2), Decimal(3))

def test_clear_history():
    """Test that calculation history can be cleared."""
    Calculator.clear_history()
    assert len(Calculations.get_history()) == 0  # ✅ Ensure history is cleared

@pytest.mark.parametrize("operand_a, operand_b, result", [(3, 2, 5), (-1, -1, -2), (0, 5, 5)])
def test_add(operand_a, operand_b, result):
    """Test the add function."""
    assert Calculator.add(operand_a, operand_b) == result

@pytest.mark.parametrize("operand_a, operand_b, result", [(5, 3, 2), (-1, -1, 0), (5, 0, 5)])
def test_subtract(operand_a, operand_b, result):
    """Test the subtract function."""
    assert Calculator.subtract(operand_a, operand_b) == result

@pytest.mark.parametrize("operand_a, operand_b, result", [(2, 3, 6), (-1, -1, 1), (0, 5, 0)])
def test_multiply(operand_a, operand_b, result):
    """Test the multiply function."""
    assert Calculator.multiply(operand_a, operand_b) == result

def test_divide():
    """Test the divide function."""
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    """Test the divide by zero exception."""
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

def test_square_root():
    """Test the square root function."""
    assert Calculator.square_root(Decimal(16)) == 4

def test_square_root_negative():
    """Test the square root of a negative number."""
    with pytest.raises(ValueError):
        Calculator.square_root(-9)

def test_execute_add():
    """Test Calculator.execute() with addition."""
    result = Calculator.execute(Decimal(5), Decimal(3), add)
    assert result == 8

def test_square_root_history():
    """Test square root calculation and ensure it's stored in history."""
    Calculator.clear_history()
    result = Calculator.square_root(Decimal(16))

    last_calc = Calculator.get_last_calculation()
    
    assert result == 4
    assert last_calc is not None  # ✅ Ensure calculation was stored
    assert last_calc.result == result

def test_invalid_operation():
    """Test invalid operation exception."""
    with pytest.raises(ValueError):
        calc = Calculation("invalid", 5, 3)
        calc.result

def test_update_operands():
    """Test updating operands."""
    calc = Calculation(Decimal(5), Decimal(3), add)
    calc.update_operands(Decimal(10), Decimal(5))
    assert calc.result == add(Decimal(10), Decimal(5))

def test_str_representation():
    """Test the string representation of the calculation"""
    calc = Calculation(Decimal(5), Decimal(3), subtract)
    assert str(calc) == "5 - 3 = 2"

def test_add_calculation():
    """Test adding a calculation to history."""
    num1 = 5
    num2 = 3
    calculation = Calculation(num1, num2, add)
    Calculations.add_calculation(calculation)
    assert len(Calculations.get_history()) > 0

def test_calculator_last_calculation():
    """Test that get_last_calculation() returns None if history is empty."""
    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None

def test_calculator_history():
    """Ensure Calculator history stores and retrieves calculations properly."""
    Calculator.clear_history()
    num1, num2 = Decimal(10), Decimal(5)
    result = Calculator.add(num1, num2)  # ✅ Perform operation and store result

    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None, "Calculator.get_last_calculation() returned None"
    assert last_calc.result == result

def test_calculator_last_calculation_after_operation():
    """Test that get_last_calculation() returns the most recent calculation."""
    Calculator.clear_history()
    num1, num2 = Decimal(7), Decimal(3)
    result = Calculator.add(num1, num2)  # ✅ Perform operation and store result

    last_calc = Calculator.get_last_calculation()
    assert last_calc is not None, "Calculator.get_last_calculation() returned None"
    assert last_calc.result == result

def test_calculation_result():
    """Test that the result property correctly calls the operation."""
    calc = Calculation(Decimal(5), Decimal(3), add)
    assert calc.result == add(Decimal(5), Decimal(3))  # ✅ Cover line 29 in calculations.py

def test_square_root_execute():
    """Test Calculator.execute() with square root."""
    result = Calculator.execute(Decimal(16), None, square_root)  # ✅ Cover line 43 in calculator.py
    assert result == 4

def test_square_root_history():
    """Test square root calculation and ensure it's stored in history."""
    Calculator.clear_history()
    result = Calculator.square_root(Decimal(16))  # ✅ Calls the updated function

    last_calc = Calculator.get_last_calculation()
    
    assert result == 4
    assert last_calc is not None  # ✅ Ensure calculation was stored
    assert last_calc.result == result  # ✅ This will now work

def test_get_last_calculation_empty():
    """Test get_last_calculation() when history is empty."""
    Calculator.clear_history()
    assert Calculator.get_last_calculation() is None  # ✅ Cover lines 73-75 in calculator.py
