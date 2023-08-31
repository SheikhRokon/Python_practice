def calculate_grade(score):
    if score >= 80:
        return 'A+'
    elif score >= 79:
        return 'A'
    elif score >= 69:
        return 'A -'
    elif score >= 59:
        return 'B'
    elif score >= 49:
        return 'C'
    elif score >= 39:
        return 'D'
    else:
        return 'F'

# Input the student's score
try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Invalid score. Score should be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric score.")
