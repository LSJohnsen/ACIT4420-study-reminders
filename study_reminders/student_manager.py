
import json

class StudentsManager:

    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return "\n\n No JSON file containign student information was found."

    def add_students(self, name, email, course, preferred_time="08:00AM"):
        student = {
            "name": name,
            "email": email,
            "course": course,
            "preferred_time": preferred_time
        }

        self.students.append(student)
        self.save_students()

    def remove_students(self, name):
        self.students = [s for s in self.students if s["name"] != name]
        self.save_students()

    def save_students(self):
        with open(self.file_path, "w") as file:
            json.dump(self.students, file, indent=4)
    
    def get_students(self):
        return self.students
    
    def list_students(self):
        for student in self.students:
            print(f"Name: {student['name']}, Email: {student['email']}, Course: {student['course']}, preferred time: {student['preferred_time']}")


