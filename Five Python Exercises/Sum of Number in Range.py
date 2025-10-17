# Function definition
def sum_range(start, end):
    if start <= end:
        return sum(range(start, end + 1))
    else:
        return "Error: Start value should be less than or equal to end value."


# Main program
start_num = int(input("Enter the start number: "))  # Get start value
end_num = int(input("Enter the end number: "))      # Get end value

result = sum_range(start_num, end_num)  # Call the function
print(f"The sum of numbers from {start_num} to {end_num} is: {result}")

