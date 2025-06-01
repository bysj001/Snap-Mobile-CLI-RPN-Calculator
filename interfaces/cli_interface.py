from interfaces.interface import CalculatorInterface
from calculator.rpn_calculator import RPNCalculator

class CliInterface(CalculatorInterface):

    def __init__(self):
        self.calc = RPNCalculator()

    def run(self):

        print("RPN Calculator (CLI Mode)")
        print("Type 'q' to quit")

        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                print("Invalid input. Please enter positive real numbers and listed operators: [*, -, +, /] or 'q' to quit")

            if line.lower() == 'q':
                break
            if not line:
                continue

            tokens = line.split()

            try:
                result = self.calc.runCalculation(tokens)
                print(result)
            except Exception as e:
                print(f"Error: {e}")


            