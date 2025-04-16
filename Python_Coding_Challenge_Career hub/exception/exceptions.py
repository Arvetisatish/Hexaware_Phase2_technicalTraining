class InvalidEmailException(Exception):
    def __init__(self, message="Invalid email format. Please enter a valid email address."):
        super().__init__(message)


class SalaryException(Exception):
    def __init__(self, message="Salary cannot be negative or zero."):
        super().__init__(message)


class FileUploadException(Exception):
    def __init__(self, message="File upload error. File not found or unsupported format."):
        super().__init__(message)


class ApplicationDeadlineException(Exception):
    def __init__(self, message="Application deadline has passed. Cannot apply for this job."):
        super().__init__(message)


class DatabaseConnectionException(Exception):
    def __init__(self, message="Error connecting to the database."):
        super().__init__(message)
