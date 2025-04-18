class TaxCalculationException(Exception):
    """Exception raised when tax calculation fails."""
    def __init__(self, message="Error calculating tax for the employee."):
        self.message = message
        super().__init__(self.message)
