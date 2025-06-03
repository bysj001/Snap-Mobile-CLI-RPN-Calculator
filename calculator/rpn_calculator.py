from calculator.operations import Operations

class RPNCalculator:

    def __init__(self):
        self.stack = []
        self.operator = Operations()
    
    def runCalculation(self, tokens: list[str]) -> float:

        for token in tokens:
            if self.operator.isOperator(token):
                if len(self.stack) < 2:
                    raise ValueError(f"Not enough operands for '{token}'")
                a = self.stack.pop()
                b = self.stack.pop()
                result = self.operator.calculate(token, b, a)
                self.stack.append(result)
            else:
                try:
                    self.stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid token: '{token}' is not a number or supported operator")
                
        if self.stack:
            return self.stack[-1]
        else:
            return 0.0