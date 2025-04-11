class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds to make the payment."):
        super().__init__(message)
