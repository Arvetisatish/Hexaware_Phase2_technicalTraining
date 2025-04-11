class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data provided."):
        super().__init__(message)
