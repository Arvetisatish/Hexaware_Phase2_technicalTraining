from datetime import date
from typing import List

class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, date_of_birth: date, email: str, phone_number: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments: List['Enrollment'] = []
        self.payments: List['Payment'] = []

    def enroll_in_course(self, course, enrollment_date: date):
        from entity.enrollment import Enrollment
        enrollment = Enrollment(0, self, course, enrollment_date)
        self.enrollments.append(enrollment)

    def make_payment(self, amount: float, payment_date: date):
        from entity.payment import Payment
        payment = Payment(0, self, amount, payment_date)
        self.payments.append(payment)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}")

    def get_enrolled_courses(self):
        return [e.course for e in self.enrollments]

    def get_payment_history(self):
        return self.payments
