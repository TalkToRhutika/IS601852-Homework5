from app.commands import Command
from decimal import Decimal, InvalidOperation

class SubtractCommand(Command):
    """SubtractCommand subtracts two numbers."""

    def execute(self, *args):
        if len(args) != 2:
            print("Error: 'subtract' command requires exactly 2 arguments.")
            return
        
        try:
            a = Decimal(args[0])
            b = Decimal(args[1])
            result = a - b
            print(f"The result of {a} - {b} is {result}")
        except InvalidOperation:
            print("Error: Invalid numbers. Please provide valid numeric inputs.")  # ✅ Fix
        except Exception as e:
            print(f"Unexpected error: {e}")
