from calculator.operations import Operations

class RPNCalculator:

    def __init__(self):
        self.stack = []
        self.operator = Operations()
    
    def runCalculation(self, tokens: list[str]) -> float:

        for token in tokens:
            if self.operator.isOperator(token):
                if len(self.stack) < 2:
                    raise ValueError("Not enough operands for operation")
                a = self.stack.pop()
                b = self.stack.pop()
                result = self.operator.calculate(token, b, a)
                self.stack.append(result)
            else:
                self.stack.append(float(token))

        if self.stack:
            return self.stack[-1]
        else:
            return 0.0