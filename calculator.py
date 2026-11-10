import math
add = "+"
sub = "-"
mult = "*"
div = "/"
powr = "**"
mod = "%"

while True:
    num1 = float(input("Enter first number: "))
    operator = str(input("Enter operator: "))
    num2 = float(input("Enter second number: "))

    if operator == add:
        result = num1 + num2
    elif operator == sub:
        result = num1 - num2
    elif operator == mult:
        result = num1 * num2
    elif operator == div:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    elif operator == powr:
        result = num1 ** num2
    elif operator == mod:
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error: Modulo by zero"
    else:
        result = "Error: Invalid operator"

    if isinstance(result, str):
        print("Result:", result)
    else:
        print("Result:", int(result))
    