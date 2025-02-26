import math
from app.commands import Command

class SquareRootCommand(Command):
    def execute(self, *args):
        if len(args) != 1:
            print("Error: Square root command requires exactly 1 argument.")
            return

        try:
            num = float(args[0])
            if num < 0:
                print("Error: Cannot calculate square root of a negative number.")
                return

            result = math.sqrt(num)
            print(f"The square root of {int(num)} is {result:.2f}")  # ✅ Ensure integer input formatting
        except ValueError:
            print("Error: Invalid input. Please provide a valid number.")
