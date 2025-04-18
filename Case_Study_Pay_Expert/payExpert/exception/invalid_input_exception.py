class InvalidInputException(Exception):
    """Exception raised for invalid input data."""
    def __init__(self, message="Invalid input provided."):
        self.message = message
        super().__init__(self.message)
