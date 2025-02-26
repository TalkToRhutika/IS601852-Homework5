from app.commands import Command

class PercentageCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Error: Percentage command requires exactly 2 arguments.")
            return

        try:
            base, percent = map(float, args)
            result = (percent / 100) * base
            print(f"The result of {int(percent)}% of {int(base)} is {int(result)}")  # ✅ Ensure integer output
        except ValueError:
            print("Error: Invalid input. Please provide valid numbers.")
