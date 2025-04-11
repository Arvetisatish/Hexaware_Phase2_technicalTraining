class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student is already enrolled in the course."):
        super().__init__(message)
