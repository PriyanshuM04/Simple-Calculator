from math import *

class Calculations():
    def __init__(self, num1: float, operator: str) -> None:
        self.num1 = num1
        {'+': self.add(), '-':self.subtract()}

    def add(self) -> float:
        num2 = float(input())
        result = self.num1 + num2
        return result
    
    def subtract(self) -> float:
        num2 = float(input())
        result = self.num1 - num2
        return result
    
    def multiply(self) -> float:
        num2 = float(input())
        result = self.num1 * num2
        return result
    
    def divide(self) -> float:
        num2 = float(input())
        result = self.num1 / num2
        return result
    
    def power(self) -> float:
        num2 = float(input())
        result = self.num1 ** num2
        return result


class Calculator():
    def __init__(self):
        
        methods = Calculations(self.textarea())
        # methods.add()
        
    def textarea(self):
        self.initial_value = float(input())
        self.operator = input()
        return self.initial_value, self.operator

    def clear(self):
        self.textarea = ""


if __name__ == "__main__":
    calculator = Calculator()
