class Teacher:
    def __init__(self, teacher_id: int, first_name: str, last_name: str, email: str):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_teacher_info(self, name: str, email: str):
        self.first_name, self.last_name = name.split(" ")
        self.email = email

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}")

    def get_assigned_courses(self):
        return self.assigned_courses
