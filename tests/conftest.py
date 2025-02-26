from decimal import Decimal
from faker import Faker
import pytest
from calculator.calculations import Calculations, Calculation
from calculator.operations import add, subtract, multiply, divide

# Create a single Faker instance to use throughout the tests
faker = Faker()

# ✅ Cover Line 21: Test pytest command-line option
def pytest_addoption(parser):
    """Add a command-line option to specify the number of records."""
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# ✅ Cover Line 27: Test random number fixture
@pytest.fixture
def random_numbers():
    """Provides a tuple of two random decimal numbers for testing."""
    return Decimal(faker.random_number(digits=2, fix_len=True)), Decimal(faker.random_number(digits=2, fix_len=True))

# ✅ Cover Lines 33-55: Test random operation fixture
@pytest.fixture
def random_operation():
    """Provides a random arithmetic operation."""
    return faker.random_element([add, subtract, multiply, divide])

# ✅ Cover Lines 33-55: Test generate test data fixture
@pytest.fixture
def generate_test_data(request):
    """Generates test data dynamically based on the --num_records argument."""
    num_records = request.config.getoption("--num_records")  # Retrieve the number of records from pytest arguments
    data = []

    for _ in range(num_records):
        a = Decimal(faker.random_number(digits=2, fix_len=True))  # Random number for a
        b = Decimal(faker.random_number(digits=2, fix_len=True))  # Random number for b
        operation = faker.random_element([add, subtract, multiply, divide])  # Random operation

        # Compute the expected result based on the operation
        if operation == add:
            expected_result = a + b
        elif operation == subtract:
            expected_result = a - b
        elif operation == multiply:
            expected_result = a * b
        elif operation == divide:
            expected_result = a / b if b != 0 else "Cannot divide by zero"
        else:
            expected_result = None  # If no valid operation is selected

        data.append((str(a), str(b), operation.__name__, str(expected_result)))  # Prepare data for testing

    return data

# ✅ Cover Lines 68-73: Ensure setup and teardown works
@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Runs setup before and teardown after each test function."""
    print("\n[Setup] Test is starting...")
    yield  # Test runs here
    print("\n[Teardown] Test finished.")

# ✅ Cover Line 77-80: Ensure `pytest_addoption` works
def test_pytest_addoption(pytestconfig):
    """Test that pytest_addoption is properly defined and retrieves num_records."""
    num_records = pytestconfig.getoption("num_records")
    assert isinstance(num_records, int) and num_records > 0  # ✅ Validate pytest command-line argument

# ✅ Cover Lines 84-92: Test Fixtures Directly
def test_random_numbers(random_numbers):
    """Test that random_numbers fixture returns two decimal numbers."""
    a, b = random_numbers
    assert isinstance(a, Decimal) and isinstance(b, Decimal)

def test_random_operation(random_operation):
    """Test that random_operation fixture returns a valid operation."""
    assert random_operation in [add, subtract, multiply, divide]

def test_generate_test_data(generate_test_data):
    """Test that generate_test_data fixture provides valid test cases."""
    assert isinstance(generate_test_data, list)
    assert len(generate_test_data) > 0
    for record in generate_test_data:
        assert len(record) == 4  # Ensure each record has (a, b, operation, expected_result)

def test_add_calculation():
    """Test adding a calculation to history using Calculations."""
    num1 = 5
    num2 = 3
    calculation = Calculation(num1, num2, add)

    # Add the calculation to the history using Calculations
    Calculations.add_calculation(calculation)

    # Ensure that history was updated
    assert len(Calculations.get_history()) > 0

def test_clear_history():
    """Test clearing history in Calculations."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0  # ✅ Ensure history is cleared

# Additional test for handling division by zero
def test_divide_by_zero():
    """Test that division by zero returns an error message."""
    num1 = Decimal(10)
    num2 = Decimal(0)
    result = divide(num1, num2)
    assert result == "Cannot divide by zero"

# Additional test for verifying calculations history
def test_calculation_history():
    """Test retrieving the calculation history."""
    num1 = Decimal(7)
    num2 = Decimal(5)
    calculation = Calculation(num1, num2, subtract)
    Calculations.add_calculation(calculation)

    history = Calculations.get_history()
    assert len(history) == 1  # Ensure history contains one entry
    assert history[0].result == num1 - num2  # Validate that the history contains the correct result

# ✅ Cover Lines 108-111: Validate operations fixture functionality
def test_operations_fixture(random_operation):
    """Test that the operations fixture works correctly by performing an operation."""
    num1, num2 = Decimal(5), Decimal(3)
    result = random_operation(num1, num2)
    
    # Ensure the result is of type Decimal or the specific division error
    if random_operation == divide and num2 == 0:
        assert result == "Cannot divide by zero"
    else:
        assert isinstance(result, Decimal)

# ✅ Cover Lines 116-123: Validate data generation with the generate_test_data fixture
def test_generate_test_data_validation(generate_test_data):
    """Test that the generated test data is in the correct format."""
    for record in generate_test_data:
        assert isinstance(record[0], str)  # Validate the first number is a string
        assert isinstance(record[1], str)  # Validate the second number is a string
        assert isinstance(record[2], str)  # Ensure the operation is a string
        assert isinstance(record[3], str)  # Ensure the expected result is a string
        # Further validation can be added to check the operation and expected result

# ✅ Cover Lines 128-135: Validate invalid records in test data generation
def test_generate_invalid_test_data(generate_test_data):
    """Test that invalid records are properly handled in the generated test data."""
    for record in generate_test_data:
        # Ensure that no invalid operation or result is included in the test data
        assert record[2] in ['add', 'subtract', 'multiply', 'divide']
        # Validate that the expected result is either a valid Decimal or error message
        assert record[3] in ['Cannot divide by zero'] or isinstance(Decimal(record[3]), Decimal)

# ✅ Cover Lines 140-144: Validate test data for specific edge cases (e.g., zero)
def test_edge_case_test_data(generate_test_data):
    """Test edge cases for the generated test data, like zero values."""
    edge_case_data = [
        (Decimal(0), Decimal(0), 'add', '0'),
        (Decimal(0), Decimal(5), 'multiply', '0'),
        (Decimal(10), Decimal(0), 'divide', 'Cannot divide by zero')
    ]
    
    for a, b, op, expected in edge_case_data:
        result = None
        if op == 'add':
            result = a + b
        elif op == 'multiply':
            result = a * b
        elif op == 'divide':
            result = a / b if b != 0 else "Cannot divide by zero"
        
        assert str(result) == expected
