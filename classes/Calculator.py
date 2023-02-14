import math


class Calculator:
    """
    Calculator class
    """
    def __init__(self):
        """
        Create a new Calculator object
        """
        self.current_value = 0
        self.second_value = 0
        self.memory = 0
        self.operation = None

    def add(self):
        """
        Add the current value and the second value
        :return:
        """
        self.current_value += self.second_value

    def subtract(self):
        """
        Subtract the second value from the current value
        :return:
        """
        self.current_value -= self.second_value

    def multiply(self):
        """
        Multiply the current value and the second value
        :return:
        """
        self.current_value *= self.second_value

    def divide(self):
        """
        Divide the current value by the second value
        :return:
        """
        self.current_value /= self.second_value

    def sin(self):
        """
        Calculate the sine of the current value
        :return:
        """
        self.current_value = math.sin(self.current_value)

    def cos(self):
        """
        Calculate the cosine of the current value
        :return:
        """
        self.current_value = math.cos(self.current_value)

    def tan(self):
        """
        Calculate the tangent of the current value
        :return:
        """
        self.current_value = math.tan(self.current_value)

    def log(self):
        """
        Calculate the log of the current value
        :return:
        """
        self.current_value = math.log(self.current_value)

    def sqrt(self):
        """
        Calculate the square root of the current value
        :return:
        """
        self.current_value = math.sqrt(self.current_value)

    def exp(self):
        """
        Calculate the exponential of the current value
        :return:
        """
        self.current_value = math.exp(self.current_value)

    def clear(self):
        """
        Clear the calculator
        :return:
        """
        self.current_value = 0
        self.second_value = 0
        self.operation = None

    def evaluate(self):
        """
        Evaluate the current operation
        :return:
        """
        if self.operation == "+":
            self.add()
        elif self.operation == "-":
            self.subtract()
        elif self.operation == "*":
            self.multiply()
        elif self.operation == "/":
            self.divide()
        elif self.operation == "^":
            self.current_value **= self.second_value
        elif self.operation == "sin":
            self.sin()
        elif self.operation == "cos":
            self.cos()
        elif self.operation == "tan":
            self.tan()
        elif self.operation == "log":
            self.log()
        elif self.operation == "sqrt":
            self.sqrt()
        elif self.operation == "exp":
            self.exp()

