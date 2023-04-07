"""Some useless mathematical utility functions."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def sub(a, b):
    """Substract b from a."""
    return a - b

def multiply(a, b):
    """Multiply a by b."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

def power(a, b):
    """Return a power b."""
    return a ** b
