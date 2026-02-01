import os
class StudentManager:
    def create(self, filename="students.txt"):
        """Initializes and creates the data file if it doesn't exist."""
        self.filename = filename
        if not os.path.exists(self.filename):
            # Create an empty file if it's missing
            open(self.filename, 'w').close()
    
    def add_student(self, name, roll, grade):
        """Saves a new student record to the text file."""
        with open(self.filename, "a") as f:
            # We use commas to separate data so we can split it later
            f.write(f"{name},{roll},{grade}\n")
        return "Student added successfully!"
   
    def view_students(self):
        """Retrieves and returns all student records from the text file."""
        students = []
        with open(self.filename, "r") as f:
            for line in f:
                name, roll, grade = line.strip().split(",")
                students.append({"name": name, "roll": roll, "grade": grade})
        return students 
    
    def search_student(self, roll):
        """Searches for a student by roll number."""
        students = self.view_students()
        for student in students:
            if student["roll"] == roll:
                return student
        return None
    
    def update_student(self, roll, name=None, grade=None):
        """Updates a student's name and/or grade."""
        students = self.view_students()
        for student in students:
            if student["roll"] == roll:
                if name:
                    student["name"] = name
                if grade:
                    student["grade"] = grade
                updated = True
        if updated:
            with open(self.filename, "w") as f:
                for student in students:
                    f.write(f'{student[name]},{student["roll"]},{student["grade"]}\n')
            return "Student record updated successfully!"
        else:
            return "Student not found"
    
    def delete_student(self, roll):
        """Deletes a student by roll number."""
        students = self.view_students()
        students = [s for s in students if s["roll"] != roll]
        with open(self.filename, "w") as f:
            for student in students:
                f.write(f'{student["name"]},{student["roll"]},{student["grade"]}\n')
        return "Student deleted successfully!"
    
# Interactive Console Menu
# -------------------------
manager = StudentManager()

while True:
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        name = input("Name: ").strip()
        roll = input("Roll: ").strip()
        grade = input("Grade: ").strip()
        print(manager.add_student(name, roll, grade))
    
    elif choice == "2":
        students = manager.view_students()
        if students:
            print("\nAll Students:")
            for s in students:
                print(f'Name: {s["name"]}, Roll: {s["roll"]}, Grade: {s["grade"]}')
        else:
            print("No students found.")
    
    elif choice == "3":
        roll = input("Roll to search: ").strip()
        student = manager.search_student(roll)
        if student:
            print(f'Student found: Name: {student["name"]}, Roll: {student["roll"]}, Grade: {student["grade"]}')
        else:
            print("Student not found.")
    
    elif choice == "4":
        roll = input("Roll to update: ").strip()
        name = input("New name (leave blank to skip): ").strip()
        grade = input("New grade (leave blank to skip): ").strip()
        result = manager.update_student(roll, name or None, grade or None)
        print(result)
    
    elif choice == "5":
        roll = input("Roll to delete: ").strip()
        print(manager.delete_student(roll))
    
    elif choice == "6":
        print("Exiting Student Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice! Try again.")
    