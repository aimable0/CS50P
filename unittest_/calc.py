def add(x, y):
    """add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError("Can not divide by Zero!")
    return x / y
