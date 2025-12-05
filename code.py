import json

# JSON File load + save functions
def load_data():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)


#STUDENT CLASS (OOP) 
class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }


#MAIN OPERATIONS


# Add Student
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    s = Student(name, age, course, marks)
    data = load_data()
    data.append(s.to_dict())
    save_data(data)

    print("Student added successfully!")

# View Students
def view_students():
    print("\n--- Student List ---")
    data = load_data()
    if not data:
        print("No students found.")
        return

    for s in data:
        print(f"Name: {s['name']}, Age: {s['age']}, Course: {s['course']}, Marks: {s['marks']}")

# Search Student
def search_student():
    print("\n--- Search Student ---")
    target = input("Enter student name: ")
    data = load_data()

    for s in data:
        if s["name"].lower() == target.lower():
            print("Found Student:", s)
            return
    print("Student not found.")

# Update Marks
def update_marks():
    print("\n--- Update Marks ---")
    target = input("Enter name: ")
    data = load_data()

    for s in data:
        if s["name"].lower() == target.lower():
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            save_data(data)
            print("Marks updated successfully!")
            return

    print("Student not found.")

# Delete Student
def delete_student():
    print("\n--- Delete Student ---")
    target = input("Enter name: ")
    data = load_data()

    new_data = [s for s in data if s["name"].lower() != target.lower()]

    if len(new_data) == len(data):
        print("Student not found.")
        return

    save_data(new_data)
    print("Student deleted successfully!")

# Top Scorers (List Comprehension)
def top_scorers():
    print("\n--- Top Scorers (90+) ---")
    data = load_data()

    top = [s for s in data if s["marks"] >= 90]

    if not top:
        print("No top scorers found.")
        return

    for s in top:
        print(s)


#MENU SYSTEM
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Top Scorers")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            top_scorers()
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
menu()
