from app.commands import Command
from decimal import Decimal, InvalidOperation

class DivideCommand(Command):
    """Command to divide two decimal numbers."""

    def execute(self, *args):
        """Executes the division command with the provided arguments."""
        if len(args) != 2:
            print("Error: 'divide' command requires exactly 2 arguments.")
            return

        try:
            a = Decimal(args[0])
            b = Decimal(args[1])

            if b == 0:
                print("Error: Division by zero.")
                return

            result = a / b
            print(f"The result of {a} / {b} is {result:.1f}")  # ✅ Ensure decimal output

        except InvalidOperation:
            print("Error: Please provide valid numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")
