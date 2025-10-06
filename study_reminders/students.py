


class Students:
    def __init__(self):
        self.students = []


    # Method to add new student to list
    def add_student(self, name, email, course, preferred_time="08':00AM"):
        student = {
            "name": name,
            "email": email,
            "course": course,
            "preferred_time": preferred_time
        }

        self.students.append(student)

    # Method to remove student from list
    def remove_student(self, name):
        self.students = [s for s in self.students if s["name"] != name]

    # Method to return list of students
    def get_students(self):
        return self.students