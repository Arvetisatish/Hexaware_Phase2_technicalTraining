class PayrollGenerationException(Exception):
    """Exception raised when payroll generation fails."""
    def __init__(self, message="Error generating payroll for the employee."):
        self.message = message
        super().__init__(self.message)
