import logging
from app.commands import Command

class SubtractCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a - b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        logging.info(f'{a} - {b} = {self.evaluate(a, b)}')
        print(f'{a} - {b} = {self.evaluate(a, b)}')

# from app.commands import Command
# from decimal import Decimal, InvalidOperation
# import logging

# class SubtractCommand(Command):
#     """SubtractCommand subtracts two numbers."""

#     def execute(self, *args):
#         if len(args) != 2:
#             print("Error: 'subtract' command requires exactly 2 arguments.")
#             return
        
#         try:
#             a = Decimal(args[0])
#             b = Decimal(args[1])
#             result = a - b
#             logging.info(f'{a} - {b} = {self.evaluate(a, b)}')
#             print(f"The result of {a} - {b} is {result}")
#         except InvalidOperation:
#             print("Error: Invalid numbers. Please provide valid numeric inputs.")
#         except Exception as e:
#             print(f"Unexpected error: {e}")