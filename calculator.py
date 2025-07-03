
# calculator.py - Math operations module
print(f"Loading calculator.py: __name__ = {__name__}")

def add(a, b):
    """Add two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def power(a, b):
    """Raise a to the power of b"""
    return a ** b

# This only runs if calculator.py is executed directly
if __name__ == "__main__":
    print("calculator.py is being run directly!")
    print("Testing functions:")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
else:
    print("calculator.py has been imported as a module")