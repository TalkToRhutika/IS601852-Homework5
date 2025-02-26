from app.commands import Command

class ExitCommand(Command):
    """
    ExitCommand is a command that exits the program when executed.
    """

    def execute(self):
        """
        Executes the exit command, prints an exit message, and terminates the program.
        """
        print("Exiting...")
        raise SystemExit
