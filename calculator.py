#  Calculator in Python

def calculator():
    print("Welcome to the Calculator!")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter the operation (1/2/3/4): ")

    # Perform calculation
    if operation == '1' or operation == '+':
        result = num1 + num2
        op_symbol = '+'
    elif operation == '2' or operation == '-':
        result = num1 - num2
        op_symbol = '-'
    elif operation == '3' or operation == '*':
        result = num1 * num2
        op_symbol = '*'
    elif operation == '4' or operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        op_symbol = '/'
    else:
        print("Invalid operation selected.")
        return

    # Display result
    print(f"Result: {num1} {op_symbol} {num2} = {result}")


# Run the calculator
calculator()
