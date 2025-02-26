## ABC : Abstract Base Class 
- It allows you to define a class that cannot be instantiated directly but can serve as a blueprint for other classes.
- @abstractmethod: A decorator that defines an abstract method. Any subclass inheriting from this abstract class must implement this method; otherwise, it will raise an error.

### Command Class : inherited from ABC
- It provides a structure for all command-related classes.
- The execute method is an abstract method, meaning any class inheriting from Command must implement the execute method.
- *args allows the method to accept a variable number of arguments.
  
### Command Handler Class
- __init__ method initializes an empty dictionary commands to store the command name and corresponding Command object.

### Registering Commands
- This method adds the provided command object to the commands dictionary with command_name as the key. 
- It allows dynamic registration of multiple commands.

### Executing Commands
- It takes a user input string.
- If no input is provided, it prints a message and exits.

### Executing the Corresponding Command
- This allows handling multiple commands with different arguments in a robust and dynamic way.

