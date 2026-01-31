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
        
    