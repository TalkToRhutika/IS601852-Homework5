from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide, percentage, square_root

def test_operations():
    assert add(Decimal('2'), Decimal('3')) == Decimal('5')
    assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')
    assert multiply(Decimal('2'), Decimal('3')) == Decimal('6')
    assert divide(Decimal('6'), Decimal('2')) == Decimal('3')
    assert percentage(Decimal('50'), Decimal('10')) == Decimal('5')
    assert square_root(Decimal('9')) == Decimal('3')
    #assert factorial(Decimal('4')) == 24

    with pytest.raises(ValueError):
        divide(Decimal('5'), Decimal('0'))
    with pytest.raises(ValueError):
        square_root(Decimal('-1'))
    # with pytest.raises(ValueError):
    #     factorial(Decimal('3.5'))
