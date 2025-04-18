class EmployeeNotFoundException(Exception):
    """Exception raised when an employee is not found in the database."""
    def __init__(self, message="Employee not found in the database."):
        self.message = message
        super().__init__(self.message)
