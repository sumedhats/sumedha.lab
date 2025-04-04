# Simple Calculator Program

# Function to perform the calculations
def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")

    # Get user input for the operation
    try:
        operation = input("Please choose an operation (1-7): ")

        if operation not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid input, please choose a valid operation.")
            return

        # Get user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if operation == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")

        elif operation == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")

        elif operation == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")

        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")

        elif operation == '5':
            result = num1 % num2
            print(f"The result of {num1} % {num2} is: {result}")

        elif operation == '6':
            result = num1 ** num2
            print(f"The result of {num1} ** {num2} is: {result}")

        elif operation == '7':
            result = num1 // num2
            print(f"The result of {num1} // {num2} is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Call the calculator function
calculator()

