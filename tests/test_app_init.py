import pytest
from unittest.mock import patch
from app import App
from app.commands import CommandHandler

@pytest.fixture
def app_instance():
    """Fixture to create an App instance."""
    return App()

@patch('builtins.input', side_effect=['exit'])
def test_app_start_exits_immediately(mock_input, app_instance):
    assert mock_input  
    with pytest.raises(SystemExit):
        app_instance.start()

@patch('builtins.input', side_effect=['invalidcommand 5 3', 'exit'])
@patch.object(CommandHandler, 'execute_command', return_value=None)
def test_app_invalid_command(mock_execute, mock_input, app_instance, capsys):
    assert mock_input  
    assert mock_execute  

    with pytest.raises(SystemExit):
        app_instance.start()

    captured = capsys.readouterr()
    assert "Error: Unknown command" in captured.out  # ✅ Match test output

@patch('builtins.input', side_effect=['add a b', 'exit'])
def test_app_invalid_numbers(mock_input, app_instance, capsys):
    assert mock_input  
    with pytest.raises(SystemExit):
        app_instance.start()

    captured = capsys.readouterr()
    assert "Error: Invalid numbers. Please enter valid decimal numbers." in captured.out  

@patch('builtins.input', side_effect=['add 5 3', 'exit'])
@patch.object(CommandHandler, 'execute_command', return_value=8)
def test_app_history_updates_correctly(mock_execute, mock_input, app_instance, capsys):
    assert mock_input  
    assert mock_execute  

    with pytest.raises(SystemExit):
        app_instance.start()

    captured = capsys.readouterr()
    assert "Result: 8" in captured.out  
    assert (5, 3, 8) in app_instance.history  
