# ============================================================
# Author: Your Name
# Date: 2026-06-14
# Description: Basic calculator functions
# ============================================================

# functions
def add(a, b):
    return sum([a, b]);

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b;

def divide(a, b):
    return a / b;
def power(base, exp):
    """
    Raises base to the power of exp.

    Args:
        base (int | float): The base number.
        exp (int): The exponent.

    Returns:
        float: Result of base ** exp.

    Raises:
        ValueError: If exp is negative.
        TypeError: If inputs are not numbers.
    """
    if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
        raise TypeError("base and exp must be numbers")
    if exp < 0:
        raise ValueError("Negative exponents are not supported")
    return base ** exp

def modulo(a, b):
    return a % b;