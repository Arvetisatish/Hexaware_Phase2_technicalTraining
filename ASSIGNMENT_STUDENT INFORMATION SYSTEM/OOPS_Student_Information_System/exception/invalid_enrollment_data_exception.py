class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data provided."):
        super().__init__(message)
