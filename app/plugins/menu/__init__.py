from app.commands import Command

class MenuCommand(Command):
    """
    MenuCommand is a command that displays the list of available commands.
    """

    def __init__(self, command_handler):
        """
        Initializes the MenuCommand with the command handler instance.

        Args:
            command_handler (CommandHandler): The handler responsible for managing commands.
        """
        self.command_handler = command_handler

    def execute(self):
        """
        Displays the list of available commands.
        """
        if not self.command_handler.commands:
            print("No available commands.")
            return
        # else:
        #     print("Available commands:")
        #     for command_name in self.command_handler.commands.keys():
        #         print(f" - {command_name}")
