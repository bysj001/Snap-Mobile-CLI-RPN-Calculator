from interfaces.interface import CalculatorInterface
from calculator.rpn_calculator import RPNCalculator
import sys

class CliInterface(CalculatorInterface):

    def __init__(self):
        self.calc = RPNCalculator()

    def run(self):
        print("\n" + "=" * 40)
        print("RPN Calculator (CLI Mode)")
        print("=" * 40)
        print("Instructions:")
        print(" • Enter expressions using Reverse Polish Notation (RPN)")
        print(" • Supported operations: +   -   *   /")
        print(" • Example: To compute (3 + 4), enter: 3 4 +")
        print(" • Example: To compute (5 * (3 + 2)), enter: 3 2 + 5 *")
        print(" • Type 'q' to quit")
        print(" • Type 'clear' to clear stack")
        print("=" * 40 + "\n")

        while True:
            try:
                line = input("> ").strip()
            except EOFError:
                print("\nEOF detected. Exiting.")
                break

            if not line:
                continue

            if line.lower() == 'q':
                print("Thank you for using the RPN Calculator. Goodbye!")
                break
            
            if line.lower() == 'clear':
                self.calc.stack.clear()
                print("\n Stack cleared. \n")
                continue

            tokens = line.split()

            try:
                result = self.calc.runCalculation(tokens)
                print(result)
            except ValueError as e:
                print(f"Error: {e}. This input will be ignored. Please try again.")
            except ZeroDivisionError as e:
                print(f"Error: {e}. Cannot divide by zero. This input will be ignored.")
            except Exception as e:
                print(f"Error: {e}")