students = {
    "S001": {
        "name": "Alex",
        "subject": "Maths",
        "mark": 85
    },
    "S002": {
        "name": "Sam",
        "subject": "Science",
        "mark": 78
    },
    "S003": {
        "name": "Jamie",
        "subject": "English",
        "mark": 92
    },
    "S004": {
        "name": "Alex",
        "subject": "Maths",
        "mark": 85
    }
}

print("Student records:")
print(students)

print(students["S001"])

print(students.get("S005", "Student not found"))

students["S005"] = {
    "name": "Taylor",
    "subject": "Art",
    "mark": 88
}

students["S002"]["mark"] = 90

students.pop("S003")

if students["S004"] == students["S001"]:
    students.pop("S004")

print("Number of students:", len(students))

for student_id, details in students.items():
    print(student_id, details["name"], details["subject"], details["mark"])