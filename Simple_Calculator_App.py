# Simple Calculator App
# This program can perform addition, subtraction, multiplication, and division.

def calculator():
    print(" Simple Calculator")
    print("Choose operation: +, -, *, /")

    # Take user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+ - * /): ")
    num2 = float(input("Enter second number: "))

    # Perform operation based on operator
    if operator == "+":
        print(f"Result = {num1 + num2}")
    elif operator == "-":
        print(f"Result = {num1 - num2}")
    elif operator == "*":
        print(f"Result = {num1 * num2}")
    elif operator == "/":
        if num2 != 0:
            print(f"Result = {num1 / num2}")
        else:
            print(" Division by Zero not allowed!")
    else:
        print(" Invalid Operator")

# Run the calculator
calculator()
