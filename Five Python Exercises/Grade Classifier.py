    # Function definition
def classify_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score. Please enter a value between 0 and 100.'


# Main program
score = float(input("Enter your score (0-100): "))  # Get score from user
grade = classify_grade(score)  # Call the function
print(f"Your grade is: {grade}")
