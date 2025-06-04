import unittest
from unittest.mock import patch
from interfaces.cli_interface import CliInterface


class TestCliIntegration(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "10", "+", "15", "+", "q"])
    @patch('builtins.print')
    def test_three_number_addition(self, mock_print, _):
        cli = CliInterface()
        cli.run()
        output = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn(30.0, output)

    @patch('builtins.input', side_effect=["10", "0", "/", "q"])
    @patch('builtins.print')
    def test_division_by_zero_error(self, mock_print, _):
        cli = CliInterface()
        cli.run()
        output = [call.args[0] for call in mock_print.call_args_list]
        self.assertTrue(any("Division by zero" in str(line) for line in output))

    @patch('builtins.input', side_effect=["1", "+", "q"])
    @patch('builtins.print')
    def test_insufficient_operands_error(self, mock_print, _):
        cli = CliInterface()
        cli.run()
        output = [call.args[0] for call in mock_print.call_args_list]
        self.assertTrue(any("Not enough operands" in str(line) for line in output))

    @patch('builtins.input', side_effect=["1", "2", "+", "q"])
    @patch('builtins.print')
    def test_valid_addition_then_quit(self, mock_print, _):
        cli = CliInterface()
        cli.run()
        output = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn(3.0, output)
        self.assertIn("Thank you for using the RPN Calculator. Goodbye!", output)

    @patch('builtins.input', side_effect=["q"])
    @patch('builtins.print')
    def test_quit(self, mock_print, _):
        cli = CliInterface()
        cli.run()
        output = [call.args[0] for call in mock_print.call_args_list]
        self.assertIn("Thank you for using the RPN Calculator. Goodbye!", output)


if __name__ == '__main__':
    unittest.main()
