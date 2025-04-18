class DatabaseConnectionException(Exception):
    """Exception raised when a database connection issue occurs."""
    def __init__(self, message="Database connection failed."):
        self.message = message
        super().__init__(self.message)
