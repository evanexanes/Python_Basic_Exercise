def calculate(num1, num2, operation):  # define function
    if operation == 'add':  # if-else statement process
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero"
    else:
        return "Error: Invalid operation"


# Test cases
result = calculate(1, 2, 'add')
print(f"The result of adding 1 and 2 is {result}")

result = calculate(1, 2, 'subtract')
print(f"The result of subtracting 1 and 2 is {result}")

result = calculate(1, 2, 'multiply')
print(f"The result of multiplying 1 and 2 is {result}")

result = calculate(1, 2, 'divide')
print(f"The result of dividing 1 and 2 is {result}")
