class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def subtract(self, num1, num2):
        self.result = num1 - num2

    def multiply(self, num1, num2):
        self.result = num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            self.result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")

    def clear(self):
        self.result = 0


calculator = Calculator()

calculator.add(2, 2)
print("Result:", calculator.result)

calculator.multiply(6, 5)
print("Result:", calculator.result)

calculator.divide(15, 3)
print("Result:", calculator.result)
