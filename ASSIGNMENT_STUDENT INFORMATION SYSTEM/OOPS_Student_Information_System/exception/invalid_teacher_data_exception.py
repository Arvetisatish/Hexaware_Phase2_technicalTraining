class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data provided."):
        super().__init__(message)
