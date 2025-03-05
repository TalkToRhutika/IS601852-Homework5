from app.commands import Command
import logging

class AddCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a + b

    def execute(self, *args, **kwargs):
        # Ensure args are converted to floats
        a, b = map(float, args)
        logging.info(f'{a} + {b} = {self.evaluate(a, b)}')
        print(f'{a} + {b} = {self.evaluate(a, b)}')

# from app.commands import Command
# from decimal import Decimal, InvalidOperation
# import logging

# class AddCommand(Command):
#     """Command to add two decimal numbers."""

#     def execute(self, *args):
#         """Executes the addition command with the provided arguments."""
#         if len(args) != 2:
#             print("Error: 'add' command requires exactly 2 arguments.")
#             return

#         try:
#             a = Decimal(args[0])
#             b = Decimal(args[1])
#             result = a + b
#             logging.info(f'{a} + {b} = {self.evaluate(a, b)}')
#             print(f"The result of {a} + {b} is {result}")
#         except InvalidOperation:
#             print("Invalid input: Please provide valid numbers.")
#         except Exception as e:
#             print(f"Unexpected error: {e}")