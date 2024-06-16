# import math as m
import numpy as np

class Calculator:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def add(self):
        result = self.num1 + self.num2
        return result

    def subtract(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        result = self.num1 / self.num2
        return result

    def power(self):
        result = self.num1 ** self.num2
        return result

    def matrix(self):
        pass


if __name__ == "__main__":
    operators = {'+': "calc.add()", '-': "calc.subtract()", '*': "calc.multiply()", '/': "calc.divide()",
                 '^': "calc.power()"}
    result = 0
    loop = True
    while loop:
        num1 = float(input("Number = "))
        oper = input("Operator(+,-,*,/,^): ")
        if oper in operators.keys():
            result = num1
            num2 = float(input("Number = "))
            calc = Calculator(result, num2, oper)
            result = operators[oper]                        # ERROR SOMEWHERE
            print(calc)

        elif oper == '=':
            print(result)
            loop = False

        else:
            print("Invalid Operator!")
            oper = input("Operator(+,-,*,/,^): ")
