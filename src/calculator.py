def add(a, b):
    return a + b

# Fixed typo: renamed `subtrct` to `subtract` and kept a backwards-compatible alias

def subtract(a, b):
    return a - b

# Backwards compatibility for previous typo
subtrct = subtract


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


