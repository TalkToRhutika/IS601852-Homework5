import math
from app.commands import Command
import logging

class SquareRootCommand(Command):
    @staticmethod
    def evaluate(num: float) -> float:
        """Calculate the square root of a given number."""
        return math.sqrt(num)

    def execute(self, *args, **kwargs):
        """Execute the square root calculation command."""
        if len(args) != 1:
            print("Error: Square root command requires exactly 1 argument.")
            return

        try:
            num = float(args[0])
            if num < 0:
                print("Error: Cannot calculate square root of a negative number.")
                return

            result = self.evaluate(num)
            logging.info(f'Calculating square root of {num}: Result = {result:.2f}')
            print(f"The square root of {num} is {result:.2f}")
        except ValueError:
            print("Error: Invalid input. Please provide a valid number.")
