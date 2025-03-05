import os
import sys
import pkgutil
import importlib
import decimal
from decimal import Decimal
from dotenv import load_dotenv
import logging
import logging.config
from app.commands import Command, CommandHandler

class App:
    def __init__(self):
        """Constructor that initializes the command handler and calculation history."""
        os.makedirs('logs', exist_ok=True)
        self.command_handler = CommandHandler()
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'DEVELOPMENT')
        self.history = []

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        """Starts the REPL (Read, Evaluate, Print, Loop) for accepting user commands."""
        print("Calculator App")
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")

        try:
            while True:
                user_input = input(">>> ").strip()
                user_input_parts = user_input.split(" ")

                if not user_input_parts:
                    continue

                command_name = user_input_parts[0]

                if command_name == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)

                # Handle square_root command with a single argument
                if command_name == "square_root" and len(user_input_parts) == 2:
                    try:
                        num = Decimal(user_input_parts[1])
                        if num < 0:
                            print("Error: Cannot calculate square root of a negative number.")
                            continue
                        result = self.command_handler.execute_command(command_name, num)
                        # Check for result being None and handle accordingly
                        if result is None:
                            print("Error: Unable to calculate square root.")
                        else:
                            print(f"The square root of {num} is {result:.2f}")
                    except decimal.InvalidOperation:
                        print("Error: Invalid number. Please provide a valid decimal number.")
                    continue  # Skip the rest of the code for square_root

                # For other commands, expect two arguments
                if len(user_input_parts) != 3:
                    print("Error: Invalid input. Usage: <command> <num1> <num2>")
                    print("Available commands: add, subtract, multiply, divide, percentage, square_root, exit")
                    print("Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit.")
                    raise SystemExit(0)

                command, num1_str, num2_str = user_input_parts

                try:
                    num1 = Decimal(num1_str)
                    num2 = Decimal(num2_str)
                except decimal.InvalidOperation:
                    print("Error: Invalid numbers. Please enter valid decimal numbers.")
                    raise SystemExit(0)

                if command not in self.command_handler.commands:
                    print("Error: Unknown command")
                    print("Available commands: add, subtract, multiply, divide, percentage, square_root, exit")
                    print("Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit.")
                    raise SystemExit(0)

                result = self.command_handler.execute_command(command, num1, num2)

                if result is not None:
                    print(f"Result: {result}")
                    self.history.append((num1, num2, result))
                else:
                    print("Error: Unable to execute the command.")

        except KeyboardInterrupt:
            print("\nExiting...")
            logging.error(f"Error executing command: {command_name}. Exception")
            raise SystemExit(0)
        except SystemExit as e:
            if e.code != 0:
                print(f"Exiting with error code {e.code}")
            raise
