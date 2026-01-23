import os
class StudentManager:
    def create(self, filename="students.txt"):
        """Initializes and creates the data file if it doesn't exist."""
        self.filename = filename
        if not os.path.exists(self.filename):
            # Create an empty file if it's missing
            open(self.filename, 'w').close()
