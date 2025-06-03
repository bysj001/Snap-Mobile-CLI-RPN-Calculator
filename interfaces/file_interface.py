# from interfaces.interface import CalculatorInterface
# from calculator.rpn_calculator import RPNCalculator

# class FileInterface(CalculatorInterface):
#     def __init__(self, input_file, output_file=None):
#         self.inputFile = input_file
#         self.outputFile = output_file
#         self.calc = RPNCalculator()

#     def run(self):
#         results = []
#         try:
#             with open(self.inputFile, "r") as f_in:
#                 for line in f_in:
#                     tokens = line.strip().split()
#                     if not tokens:
#                         continue  # skip empty lines
#                     try:
#                         answer = self.calc.runCalculation(tokens)
#                         results.append(str(answer))
#                     except Exception as e:
#                         results.append(f"Error: {e}")
#         except FileNotFoundError:
#             print(f"Input file '{self.inputFile}' not found.")
#             return

#         if self.outputFile:
#             with open(self.outputFile, "w") as f_out:
#                 for answer in results:
#                     f_out.write(answer + "\n")
#             print(f"Results written to {self.outputFile}")
#         else:
#             for answer in results:
#                 print(answer)
