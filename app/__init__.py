import pkgutil
import importlib
import decimal  # ✅ Ensure decimal module is imported
from decimal import Decimal
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        """Constructor that initializes the command handler and calculation history."""
        self.command_handler = CommandHandler()
        self.history = []

    def load_plugins(self):
        """Dynamically load all commands from plugins directory."""
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                            self.command_handler.register_command(plugin_name, item())  
                    except TypeError:
                        continue  

    def start(self):
        """Starts the REPL (Read, Evaluate, Print, Loop) for accepting user commands."""
        print("Calculator App")
        self.load_plugins()  

        try:
            while True:  
                user_input = input(">>> ").strip()

                if user_input.lower() == 'exit':
                    print("Exiting the calculator. Goodbye!")
                    print(f"Calculation History: {self.history}")
                    raise SystemExit  

                user_input_parts = user_input.split()
                if len(user_input_parts) != 3:
                    print("Error: Invalid input. Usage: <command> <num1> <num2>")
                    raise SystemExit  

                command, num1_str, num2_str = user_input_parts

                try:
                    num1 = Decimal(num1_str)
                    num2 = Decimal(num2_str)
                except decimal.InvalidOperation:
                    print("Error: Invalid numbers. Please enter valid decimal numbers.")
                    raise SystemExit  

                if command not in self.command_handler.commands:
                    print("Error: Unknown command")  # ✅ Ensure correct error message
                    raise SystemExit  

                result = self.command_handler.execute_command(command, num1, num2)

                if result is not None:
                    print(f"Result: {result}")
                    self.history.append((num1, num2, result))  

        except KeyboardInterrupt:
            print("\nExiting...")
            raise SystemExit  
        except SystemExit:
            raise  
