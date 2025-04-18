class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data provided."):
        super().__init__(message)
