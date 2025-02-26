from abc import ABC, abstractmethod

class ExitRequested(Exception):
    """Custom exception to signal the program should exit."""
    pass

class Command(ABC):
    """Abstract base class for all commands."""
    def __init__(self, description="No description provided"):
        self.description = description

    @abstractmethod
    def execute(self, *args):
        """Method that child classes must implement to execute the command."""
        pass

class CommandHandler:
    """Handles command registration and execution."""
    
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command, aliases=None):
        """Registers a command and its aliases."""
        # Store the main command
        self.commands[command_name] = command
        # If aliases are provided, register them as well
        if aliases:
            for alias in aliases:
                self.commands[alias] = command

    def list_commands(self):
        """Lists all registered commands."""
        if not self.commands:
            print("No commands registered.")
            return
        print("Available commands:")
        # List the commands and their descriptions
        for name, command in self.commands.items():
            print(f"  {name}: {command.description}")

    def execute_command(self, input_str: str):
        """Executes a command based on user input."""
        parts = input_str.strip().split()
        if not parts:
            print("No command entered.")
            return

        command_name = parts[0]
        args = parts[1:]

        try:
            # Retrieve the command using .get() to avoid KeyError
            command = self.commands.get(command_name)
            if command:
                command.execute(*args)
            else:
                print(f"Error: Unknown command '{command_name}'")
        except TypeError as e:
            # Provide a more descriptive error if there are invalid arguments
            print(f"Error: Invalid arguments for command '{command_name}'. {e}")
        except ExitRequested:
            # Gracefully handle exit requests
            raise ExitRequested
        except Exception as e:
            # Handle any unforeseen errors
            print(f"Error executing command: {e}")

class HelpCommand(Command):
    """Command to list all available commands."""
    def __init__(self, handler):
        super().__init__("Lists all available commands.")
        self.handler = handler

    def execute(self, *args):
        """Executes the help command, listing all available commands."""
        _ = args  # Suppress unused parameter warning
        self.handler.list_commands()

class ExitCommand(Command):
    """Command to handle program exit."""
    def __init__(self):
        super().__init__("Exits the program.")

    def execute(self, *args):
        """Handles program exit by raising ExitRequested."""
        _ = args  # Suppress unused parameter warning
        print("Exiting...")
        raise ExitRequested  # Raise custom exception for clean exit
