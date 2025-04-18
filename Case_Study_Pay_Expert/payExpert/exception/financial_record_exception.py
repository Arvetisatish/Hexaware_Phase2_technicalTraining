class FinancialRecordException(Exception):
    """Exception raised when financial record processing fails."""
    def __init__(self, message="Error managing financial records."):
        self.message = message
        super().__init__(self.message)
