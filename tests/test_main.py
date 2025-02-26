from decimal import Decimal
#import pytest
from calculator.calculator import Calculator, Calculations
from calculator.operations import add

def test_main_operations():
    a, b = Decimal('10'), Decimal('5')
    assert Calculator.execute(a, b, add) == Decimal('15')
    assert len(Calculations.get_history()) > 0
