from app.commands import Command
import logging

class PercentageCommand(Command):
    @staticmethod
    def evaluate(base: float, percent: float) -> float:
        """Calculate the percentage of a given number."""
        return (percent / 100) * base

    def execute(self, *args, **kwargs):
        """Execute the percentage calculation command."""
        if len(args) != 2:
            print("Error: Percentage command requires exactly 2 arguments.")
            return

        try:
            base, percent = map(float, args)
            result = self.evaluate(base, percent)
            logging.info(f'Calculating {percent}% of {base}: Result = {result}')
            print(f"The result of {percent}% of {base} is {result}")
        except ValueError:
            print("Error: Invalid input. Please provide valid numbers.")
