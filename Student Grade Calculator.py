import json
import os
from datetime import datetime

DB_FILE = "students_db.json"

# ------------------ Storage Layer ------------------
def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Core Logic ------------------
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


def calculate_gpa(percentage):
    if percentage >= 90:
        return 4.0
    elif percentage >= 80:
        return 3.7
    elif percentage >= 70:
        return 3.3
    elif percentage >= 60:
        return 3.0
    elif percentage >= 50:
        return 2.5
    elif percentage >= 40:
        return 2.0
    else:
        return 0.0


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def performance_level(percentage):
    if percentage >= 85:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Average"
    else:
        return "Poor"

# ------------------ Features ------------------
def add_student():
    data = load_data()

    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    subjects = int(input("Enter number of subjects: "))
    marks = {}

    for i in range(subjects):
        sub = input(f"Subject {i+1} name: ")
        score = float(input(f"Marks for {sub} (0-100): "))
        marks[sub] = score

    total = sum(marks.values())
    max_total = subjects * 100
    percentage = calculate_percentage(total, max_total)
    gpa = calculate_gpa(percentage)
    grade = calculate_grade(percentage)
    level = performance_level(percentage)
    status = "PASS" if percentage >= 40 else "FAIL"

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": round(percentage, 2),
        "gpa": gpa,
        "grade": grade,
        "performance": level,
        "status": status,
        "date": str(datetime.now())
    }

    data.append(student)
    save_data(data)
    print("\n✅ Student record added successfully!\n")


def view_students():
    data = load_data()
    if not data:
        print("\nNo records found.\n")
        return

    for i, s in enumerate(data, 1):
        print("="*60)
        print(f"Record {i}")
        print(f"Name: {s['name']}")
        print(f"Roll: {s['roll']}")
        print(f"Marks: {s['marks']}")
        print(f"Total: {s['total']}")
        print(f"Percentage: {s['percentage']}%")
        print(f"GPA: {s['gpa']}")
        print(f"Grade: {s['grade']}")
        print(f"Performance: {s['performance']}")
        print(f"Status: {s['status']}")
        print(f"Date: {s['date']}")


def search_student():
    data = load_data()
    roll = input("Enter roll number to search: ")

    for s in data:
        if s['roll'] == roll:
            print("\n--- Student Found ---")
            print(json.dumps(s, indent=4))
            return
    print("\n❌ Student not found!\n")


def generate_report():
    data = load_data()
    if not data:
        print("\nNo data for report.\n")
        return

    total_students = len(data)
    passed = len([s for s in data if s['status'] == 'PASS'])
    failed = len([s for s in data if s['status'] == 'FAIL'])
    avg_percentage = sum(s['percentage'] for s in data) / total_students

    print("\n====== STUDENT PERFORMANCE REPORT ======")
    print(f"Total Students: {total_students}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Average Percentage: {round(avg_percentage,2)}%")
    print("======================================\n")

# ------------------ Menu System ------------------
def menu():
    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            generate_report()
        elif choice == '5':
            print("\nSystem Closed Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice! Try again.\n")

# ------------------ Main ------------------
if __name__ == "__main__":
    menu()