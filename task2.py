def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    # Get user input
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operation.")
        return

    # Display result
    print(f"Result: {num1} {op} {num2} = {result}")

# Run the calculator
calculator()
