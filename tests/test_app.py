from unittest import mock
import pytest
from unittest.mock import patch
from app import App

@pytest.mark.parametrize("command", [
    'add 5 3',
    'subtract 10 2',
    'multiply 4 5',
    'divide 10 2',
    'percentage 50 100',
    'square_root 9'
])
def test_calculation_commands(command, monkeypatch):
    """Simulate command followed by exit."""
    inputs = iter([command, 'exit'])  # Ensure input is a string, not a list
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()  # Ensure the app start triggers SystemExit

    assert e.type == SystemExit  # Check if SystemExit was raised
    assert e.value.code == 0  # Check for clean exit (0)

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the REPL output
    captured = capfd.readouterr()

    # Verify that the unknown command message is present in the output
    assert "Error: Invalid input. Usage: <command> <num1> <num2>" in captured.out
    assert "Available commands: add, subtract, multiply, divide, percentage, square_root, exit" in captured.out
    assert "Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out

    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Clean exit after unknown command

def test_app_invalid_input_format(capfd, monkeypatch):
    """Test how the REPL handles invalid input formats."""
    # Simulate invalid input followed by 'exit'
    inputs = iter(['add 2', 'exit'])  # Missing one argument for 'add'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    # Capture the REPL output
    captured = capfd.readouterr()

    # Verify that the error message for invalid input is present in the output
    assert "Available commands: add, subtract, multiply, divide, percentage, square_root, exit" in captured.out
    assert "Type 'command number1 number2' (e.g., 'add 2 2') or 'exit' to quit." in captured.out

    # Ensure a clean exit (exit code 0)
    assert excinfo.value.code == 0  # Ensure clean exit after invalid input

def test_load_plugins_success(monkeypatch):
    # Mock the iter_modules to simulate plugin loading
    with patch('pkgutil.iter_modules') as mock_iter_modules:
        mock_iter_modules.return_value = [('path', 'add', True)]  # Simulating that "add" plugin is found
        app = App()
        with patch.object(app.command_handler, 'register_command') as mock_register_command:
            app.load_plugins()
            # Ensure that AddCommand is called once with the correct arguments
            mock_register_command.assert_called_once_with('add', mock.ANY)  # Match AddCommand correctly

def test_load_plugins_warning_when_no_plugins(monkeypatch):
    # Simulate no plugins in directory
    with patch('pkgutil.iter_modules') as mock_iter_modules:
        mock_iter_modules.return_value = []  # Simulate no plugins in directory
        app = App()
        with patch('logging.warning') as mock_warning:
            app.load_plugins()
            mock_warning.assert_called_once_with("Plugins directory 'app/plugins' not found.")  # Ensure this message is logged

def test_configure_logging_when_file_exists():
    # Simulate that logging.conf exists
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = True
        with patch('logging.config.fileConfig') as mock_file_config:
            app = App()
            app.configure_logging()
            mock_file_config.assert_called_once_with('logging.conf', disable_existing_loggers=False)  # Assert it is called only once

def test_configure_logging_when_file_does_not_exist(monkeypatch):
    # Mock load_dotenv to avoid loading environment variables during test
    monkeypatch.setattr('dotenv.main.load_dotenv', lambda: None)
    
    # Simulate that logging.conf does not exist
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        with patch('logging.basicConfig') as mock_basic_config:
            app = App()
            app.configure_logging()
            mock_basic_config.assert_called_once_with(level='INFO', format='%(asctime)s - %(levelname)s - %(message)s')

def test_start_square_root_command(monkeypatch):
    # Simulate user entering the square_root command
    inputs = iter(['square_root 25', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()

    with patch('builtins.print') as mock_print:
        with pytest.raises(SystemExit):  # Capture SystemExit
            app.start()
        mock_print.assert_called_once_with("The square root of 25 is 5.00")  # Ensure that the correct print statement is called
