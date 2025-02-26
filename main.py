import multiprocessing
from decimal import Decimal, InvalidOperation

# Example operations (add, subtract, multiply, etc.)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def percentage(a, b):
    return (a * b) / Decimal(100)

def square_root(a):
    if a < 0:
        return f"Error: Cannot calculate square root of a negative number."
    return a ** Decimal(0.5)

# Placeholder for storing the calculation history
class Calculations:
    history = []

    @classmethod
    def add_to_history(cls, a, b, result):
        cls.history.append({'a': a, 'b': b, 'result': result})

    @classmethod
    def get_history(cls):
        return cls.history


# Main Command to execute calculations
class CalculationCommand:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self):
        try:
            a_decimal = self.safe_convert(self.a)
            b_decimal = self.safe_convert(self.b)

            if self.operation == 'add':
                result = add(a_decimal, b_decimal)
            elif self.operation == 'subtract':
                result = subtract(a_decimal, b_decimal)
            elif self.operation == 'multiply':
                result = multiply(a_decimal, b_decimal)
            elif self.operation == 'divide':
                result = divide(a_decimal, b_decimal)
            elif self.operation == 'percentage':
                result = percentage(a_decimal, b_decimal)
            elif self.operation == 'square_root':
                result = square_root(a_decimal)
            else:
                result = f"Error: Unknown operation '{self.operation}'."
            
            Calculations.add_to_history(self.a, self.b, result)  # Log result to history
            return result
        except ValueError as e:
            return str(e)

    def run_async(self):
        process = multiprocessing.Process(target=self.execute_and_print)
        process.start()
        process.join()

    def execute_and_print(self):
        result = self.execute()
        print(f"Result: {result}")

    @staticmethod
    def safe_convert(value):
        try:
            return Decimal(value)
        except (InvalidOperation, ValueError):
            raise ValueError(f"Invalid input: '{value}' is not a valid number.")


# Main Application
class CalculatorApp:
    def __init__(self):
        self.running = True

    def start(self):
        print("Calculator App")
        self.show_menu()
        while self.running:
            self.run()

    def show_menu(self):
        print("\nAvailable Commands:")
        for command in ["add", "subtract", "multiply", "divide", "percentage", "square_root", "menu"]:
            print(f" - {command}")

    def run(self):
        a = input("Enter the first number (or 'exit' to quit): ")
        if a.lower() == 'exit':
            self.exit_app()
            return

        if a.lower() == 'menu':
            self.show_menu()
            return

        # Validate first input (ensure it's a number)
        try:
            a = Decimal(a)
        except ValueError:
            print(f"Error: '{a}' is not a valid number. Please try again.")
            return

        b = input("Enter the second number: ")
        # Validate second input (ensure it's a number)
        try:
            b = Decimal(b)
        except ValueError:
            print(f"Error: '{b}' is not a valid number. Please try again.")
            return

        operation = input("Enter operation (add, subtract, multiply, divide, percentage, square_root): ")

        command = CalculationCommand(a, b, operation)
        command.run_async()

    def exit_app(self):
        print("Exiting the calculator. Goodbye!")
        print("Calculation History:", [(calc['a'], calc['b'], calc['result']) for calc in Calculations.get_history()])
        self.running = False


if __name__ == "__main__":
    app = CalculatorApp()
    app.start()
