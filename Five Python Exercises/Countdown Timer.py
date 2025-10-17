# Function definition
def countdown(n):
    if n > 0:
        return list(range(n, 0, -1))
    else:
        return "Error: Please enter a positive integer."


# Main program
num = int(input("Enter a positive integer: "))  # Get user input
result = countdown(num)  # Call the function
print(f"Countdown result: {result}")
