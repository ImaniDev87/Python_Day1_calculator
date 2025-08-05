def basic_calculator():
    """
    This program creates a simple calculator that performs
    addition, subtraction, multiplication, or division
    based on user input.
    """
    print("Welcome to the Basic Calculator!")

    try:
        # Get the first number from the user
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str) # Convert input to a float to handle decimals

        # Get the second number from the user
        num2_str = input("Enter the second number: ")
        num2 = float(num2_str) # Convert input to a float

        # Get the operation from the user
        operation = input("Enter the operation (+, -, *, /): ")

        result = 0
        equation = ""

        if operation == '+':
            result = num1 + num2
            equation = f"{num1} + {num2} = {result}"
        elif operation == '-':
            result = num1 - num2
            equation = f"{num1} - {num2} = {result}"
        elif operation == '*':
            result = num1 * num2
            equation = f"{num1} * {num2} = {result}"
        elif operation == '/':
            if num2 != 0:  # Prevent division by zero
                result = num1 / num2
                equation = f"{num1} / {num2} = {result}"
            else:
                print("Error: Division by zero is not allowed.")
                return # Exit the function if division by zero occurs
        else:
            print("Invalid operation. Please choose from +, -, *, or /.")
            return # Exit the function if an invalid operation is entered

        print(equation)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to run the calculator
if __name__ == "__main__":
    basic_calculator()