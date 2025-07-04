# main.py - Main calculator program (ENTRY POINT)
print(f"Starting main.py: __name__ = {__name__}")

# Import our custom modules
import calculator
import utils

def run_calculator():
    """Main calculator logic!"""
    print("\nWelcome to the Python Calculator!")
    
    while True:
        # Display menu
        utils.display_menu()
        
        # Get user choice
        choice = utils.get_operation_choice()
        
        if choice == 5:
            print("Thank you for using the calculator! Goodbye!")
            break
        
        # Get numbers from user
        num1 = utils.get_user_input("Enter first number: ")
        num2 = utils.get_user_input("Enter second number: ")
        
        # Perform calculation based on choice
        if choice == 1:
            result = calculator.add(num1, num2)
            operation = "addition"
        elif choice == 2:
            result = calculator.multiply(num1, num2)
            operation = "multiplication"
        elif choice == 3:
            result = calculator.divide(num1, num2)
            operation = "division"
        elif choice == 4:
            result = calculator.power(num1, num2)
            operation = "power"
        
        # Display result
        formatted_result = utils.format_number(result)
        print(f"\nResult of {operation}: {formatted_result}")
        
        # Ask if user wants to continue
        continue_choice = input("\nWould you like to perform another calculation? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using the calculator! Goodbye!")
            break

def main():
    """Main function - entry point of the program"""
    print(f"\n🚀 This is the ENTRY POINT file: {__file__}")
    print("The program starts here!")
    
    try:
        run_calculator()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This is the entry point check
if __name__ == "__main__":
    print("✅ main.py is the initiating file!")
    main()
else:
    print("main.py has been imported (this shouldn't happen in this example)")