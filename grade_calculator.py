#!/usr/bin/env python3
"""
Student Grade Calculator
------------------------
This script calculates total marks, percentage, average, letter grade, 
and pass/fail status for students across various subjects.
"""

def get_letter_grade(percentage):
    """Determine the letter grade and performance based on percentage."""
    if percentage >= 90:
        return 'A+', 'Outstanding'
    elif percentage >= 80:
        return 'A', 'Excellent'
    elif percentage >= 70:
        return 'B', 'Good'
    elif percentage >= 60:
        return 'C', 'Satisfactory'
    elif percentage >= 50:
        return 'D', 'Pass'
    else:
        return 'F', 'Fail'

def calculate_student_grades(student_name, subject_scores):
    """
    Calculate results for a student given a dictionary of subject scores.
    subject_scores format: {'Subject': score}
    """
    total_subjects = len(subject_scores)
    if total_subjects == 0:
        return None

    total_marks = sum(subject_scores.values())
    max_possible = total_subjects * 100
    percentage = (total_marks / max_possible) * 100
    average_score = total_marks / total_subjects
    letter_grade, remarks = get_letter_grade(percentage)

    return {
        "name": student_name,
        "scores": subject_scores,
        "total_marks": total_marks,
        "max_possible": max_possible,
        "percentage": percentage,
        "average": average_score,
        "grade": letter_grade,
        "remarks": remarks
    }

def print_report_card(result):
    """Prints a detailed report card for a single student."""
    print("=" * 50)
    print(f"       STUDENT REPORT CARD: {result['name'].upper()}")
    print("=" * 50)
    print(f"{'Subject':<25} {'Score':<10} {'Max Marks':<10}")
    print("-" * 50)
    for subject, score in result['scores'].items():
        print(f"{subject:<25} {score:<10.2f} {100:<10}")
    print("-" * 50)
    print(f"Total Marks Obtained : {result['total_marks']:.2f} / {result['max_possible']}")
    print(f"Average Score        : {result['average']:.2f}%")
    print(f"Percentage           : {result['percentage']:.2f}%")
    print(f"Final Grade          : {result['grade']}")
    print(f"Remarks              : {result['remarks']}")
    print("=" * 50)

def run_interactive_mode():
    """Interactive CLI mode to input student details manually."""
    print("\n--- Interactive Student Grade Calculator ---")
    name = input("Enter Student Name: ").strip()
    if not name:
        name = "Student"

    subject_scores = {}
    while True:
        try:
            num_subjects = int(input("How many subjects do you want to enter? "))
            if num_subjects > 0:
                break
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(1, num_subjects + 1):
        subj = input(f"Enter Subject {i} name: ").strip()
        if not subj:
            subj = f"Subject {i}"
        while True:
            try:
                score = float(input(f"Enter score for {subj} (0-100): "))
                if 0 <= score <= 100:
                    subject_scores[subj] = score
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid score (number).")

    result = calculate_student_grades(name, subject_scores)
    print("\n")
    print_report_card(result)

def run_demo():
    """Runs a demonstration with predefined sample student data."""
    print("\n--- Running Demo Calculation ---")
    sample_data = [
        ("Alice Smith", {"Math": 95.0, "Physics": 88.5, "Chemistry": 92.0, "English": 90.0, "Computer Science": 98.0}),
        ("Bob Johnson", {"Math": 72.0, "Physics": 65.0, "Chemistry": 58.5, "English": 80.0, "History": 75.0}),
        ("Charlie Brown", {"Math": 45.0, "Physics": 48.0, "Chemistry": 52.0, "English": 55.0, "Biology": 40.0})
    ]

    for name, scores in sample_data:
        res = calculate_student_grades(name, scores)
        print_report_card(res)
        print("\n")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive_mode()
    else:
        run_demo()
