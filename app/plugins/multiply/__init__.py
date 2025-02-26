from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Error: Multiply command requires exactly 2 arguments.")
            return

        try:
            a, b = map(float, args)
            result = a * b
            print(f"The result of {int(a)} * {int(b)} is {int(result)}")  # ✅ Ensure integer output
        except ValueError:
            print("Error: Invalid numbers. Please provide valid numeric inputs.")
