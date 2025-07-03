# utils.py - Utility functions module
print(f"Loading utils.py: __name__ = {__name__}")

def format_number(num):
    """Format a number with 2 decimal places"""
    if isinstance(num, str):
        return num  # Return error messages as-is
    return f"{num:.2f}"

def get_user_input(prompt):
    """Get numeric input from user with error handling"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number!")

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*30)
    print("     CALCULATOR MENU")
    print("="*30)
    print("1. Addition")
    print("2. Multiplication") 
    print("3. Division")
    print("4. Power")
    print("5. Exit")
    print("="*30)

def get_operation_choice():
    """Get the user's operation choice"""
    while True:
        try:
            choice = int(input("Choose an operation (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please choose a number between 1 and 5!")
        except ValueError:
            print("Please enter a valid number!")

# This only runs if utils.py is executed directly
if __name__ == "__main__":
    print("utils.py is being run directly!")
    print("Testing utility functions:")
    print(f"Formatted number: {format_number(3.14159)}")
    display_menu()
else:
    print("utils.py has been imported as a module")