class Operations:
    def __init__(self):

        self.operator_map = {
            "+": self.addition,
            "-": self.subtraction,
            "*": self.multiplication,
            "/": self.division
        }

    def isOperator(self, sign: str) -> bool:
        if sign in self.operator_map:
            return True
        else:
            return False
        
    def calculate(self, sign: str, a: float, b: float) -> float:
        if not self.isOperator(sign):
            raise ValueError(f"Unsupported operator: {sign}")
        return self.operator_map[sign](a, b)
    
    def addition(self, a: float, b: float) -> float:
        return a + b
    
    def multiplication(self, a: float, b: float) -> float:
        return a * b
    
    def subtraction(self, a: float, b: float) -> float:
        return a - b
    
    def division(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b