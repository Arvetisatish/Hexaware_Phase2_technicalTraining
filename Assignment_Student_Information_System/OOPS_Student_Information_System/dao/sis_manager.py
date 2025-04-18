from datetime import date
from entity.student import Student
from entity.teacher import Teacher
from entity.course import Course
from entity.enrollment import Enrollment
from entity.payment import Payment

from exception.duplicate_enrollment_exception import DuplicateEnrollmentException
from exception.course_not_found_exception import CourseNotFoundException
from exception.student_not_found_exception import StudentNotFoundException
from exception.teacher_not_found_exception import TeacherNotFoundException
from exception.payment_validation_exception import PaymentValidationException

class SISManager:
    def __init__(self):
        self.students = {}
        self.teachers = {}
        self.courses = {}
        self.enrollments = []
        self.payments = []

    def add_student(self, student: Student):
        self.students[student.student_id] = student

    def add_teacher(self, teacher: Teacher):
        self.teachers[teacher.teacher_id] = teacher

    def add_course(self, course: Course):
        self.courses[course.course_id] = course

    def enroll_student_in_course(self, student_id: int, course_id: int, enrollment_date: date):
        if student_id not in self.students:
            raise StudentNotFoundException()
        if course_id not in self.courses:
            raise CourseNotFoundException()

        student = self.students[student_id]
        course = self.courses[course_id]

        for e in student.enrollments:
            if e.course.course_id == course_id:
                raise DuplicateEnrollmentException()

        enrollment = Enrollment(len(self.enrollments) + 1, student, course, enrollment_date)
        student.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
        self.enrollments.append(enrollment)

    def assign_teacher_to_course(self, teacher_id: int, course_id: int):
        if teacher_id not in self.teachers:
            raise TeacherNotFoundException()
        if course_id not in self.courses:
            raise CourseNotFoundException()

        teacher = self.teachers[teacher_id]
        course = self.courses[course_id]
        course.assign_teacher(teacher)
        teacher.assigned_courses.append(course)

    def record_payment(self, student_id: int, amount: float, payment_date: date):
        if student_id not in self.students:
            raise StudentNotFoundException()
        if amount <= 0:
            raise PaymentValidationException("Amount must be greater than zero.")

        student = self.students[student_id]
        payment = Payment(len(self.payments) + 1, student, amount, payment_date)
        student.payments.append(payment)
        self.payments.append(payment)

    def generate_enrollment_report(self, course_id: int):
        if course_id not in self.courses:
            raise CourseNotFoundException()
        course = self.courses[course_id]
        print(f"\nEnrollment Report for Course: {course.course_name}")
        for e in course.enrollments:
            print(f"- {e.student.first_name} {e.student.last_name} (ID: {e.student.student_id})")

    def generate_payment_report(self, student_id: int):
        if student_id not in self.students:
            raise StudentNotFoundException()
        student = self.students[student_id]
        print(f"\nPayment Report for {student.first_name} {student.last_name}:")
        for p in student.payments:
            print(f"- {p.amount} on {p.payment_date}")

    def calculate_course_statistics(self, course_id: int):
        if course_id not in self.courses:
            raise CourseNotFoundException()
        course = self.courses[course_id]
        total_enrolled = len(course.enrollments)
        total_paid = sum(p.amount for p in self.payments if p.student in [e.student for e in course.enrollments])
        print(f"\nCourse: {course.course_name}")
        print(f"Total Enrollments: {total_enrolled}")
        print(f"Total Payments Received: {total_paid}")
