import unittest
from calculator.rpn_calculator import RPNCalculator

class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = RPNCalculator()

    # Calculation Tests
    def test_pos_addition(self):
        self.assertEqual(self.calc.runCalculation(["2", "3", "+"]), 5.0)
    
    def test_neg_addition(self):
        self.assertEqual(self.calc.runCalculation(["-6", "-4", "+"]), -10.0)
        self.assertEqual(self.calc.runCalculation(["-6", "4", "+"]), -2.0)

    def test_floating_point_addition(self):
        self.assertEqual(self.calc.runCalculation(["2.5", "4.1", "+"]), 6.6)

    def test_pos_subtraction(self):
        self.assertEqual(self.calc.runCalculation(["1", "9", "-"]), -8.0)

    def test_neg_subtraction(self):
        self.assertEqual(self.calc.runCalculation(["-25", "3", "-"]), -28.0)
        self.assertEqual(self.calc.runCalculation(["-7", "-2", "-"]), -5.0)

    def test_pos_multiplication(self):
        self.assertEqual(self.calc.runCalculation(["5", "5", "*"]), 25.0)

    def test_neg_multiplication(self):
        self.assertEqual(self.calc.runCalculation(["-1", "-3", "*"]), 3.0)
        self.assertEqual(self.calc.runCalculation(["2", "-3", "*"]), -6.0)

    def test_pos_division(self):
        self.assertEqual(self.calc.runCalculation(["4", "2", "/"]), 2.0)
    
    def test_neg_division(self):
        self.assertEqual(self.calc.runCalculation(["-15", "-3", "/"]), 5.0)
        self.assertEqual(self.calc.runCalculation(["33", "-3", "/"]), -11.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.runCalculation(["5", "0", "/"])

    def test_complex_expression(self):
        self.assertEqual(self.calc.runCalculation(["3", "4", "+", "2", "*", "7", "/"]), 2.0)

    

    # Input Tests
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["2", "3", "%"])

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["+"])
        
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["+", "+"])

    def test_extra_operands_left_in_stack(self):
        self.assertEqual(self.calc.runCalculation(["2", "3", "4", "+"]), 7.0)

    def test_single_operand(self):
        self.assertEqual(self.calc.runCalculation(["42"]), 42.0)

    def test_empty_input(self):
        self.assertEqual(self.calc.runCalculation([]), 0.0)

    def test_empty_string_token(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["", "2", "+"])

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["2", "hello", "+"])

    def test_whitespace_token(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["2", " ", "3", "+"])

    def test_multiple_consecutive_operators(self):
        with self.assertRaises(ValueError):
            self.calc.runCalculation(["2", "3", "+", "+"])
    
if __name__ == '__main__':
    unittest.main()

