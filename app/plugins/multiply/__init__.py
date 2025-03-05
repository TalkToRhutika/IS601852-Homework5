import logging
from app.commands import Command

class MultiplyCommand(Command):
    @staticmethod
    def evaluate(a: float, b: float) -> float:
        return a * b

    def execute(self, *args, **kwargs):
        a, b = map(float, args)  # Convert inputs to float
        logging.info(f'{a} x {b} = {self.evaluate(a, b)}')
        print(f'{a} x {b} = {self.evaluate(a, b)}')

# from app.commands import Command
# import logging

# class MultiplyCommand(Command):
#     def execute(self, *args):
#         if len(args) != 2:
#             print("Error: Multiply command requires exactly 2 arguments.")
#             return

#         try:
#             a, b = map(float, args)
#             result = a * b
#             logging.info(f'{a} * {b} = {self.evaluate(a, b)}')
#             print(f"The result of {int(a)} * {int(b)} is {int(result)}")  
#         except ValueError:
#             print("Error: Invalid numbers. Please provide valid numeric inputs.")