# my_module.py

"""
This is a custom Python module for practice.
It contains variables, functions, and a class.
"""

# -------------------
# Variables
# -------------------
PI = 3.14159
APP_NAME = "My Practice Module"
VERSION = "1.0"

# -------------------
# Functions
# -------------------

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def factorial(n):
    """Return factorial of a number."""
    if n < 0:
        raise ValueError("Number must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


# -------------------
# Class
# -------------------

class Calculator:
    """A simple calculator class."""

    def __init__(self, name="BasicCalc"):
        self.name = name

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def info(self):
        return f"Calculator Name: {self.name}"
    
if __name__ == '__main__':
    print("Hello I am my_module.py")

    # this function will be called here itslef 
    # but if we call it outside the function it will here and where this module is importd
    print(add(1, 5)) 




