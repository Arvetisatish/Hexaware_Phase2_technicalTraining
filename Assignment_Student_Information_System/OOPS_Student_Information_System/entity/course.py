class Course:
    def __init__(self, course_id: int, course_name: str, course_code: str, instructor=None):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.enrollments = []

    def assign_teacher(self, teacher):
        self.instructor = teacher

    def display_course_info(self):
        print(f"Course ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.instructor
