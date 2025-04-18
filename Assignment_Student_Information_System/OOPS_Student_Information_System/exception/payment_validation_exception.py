class PaymentValidationException(Exception):
    def __init__(self , mesaage="Inavlid Payment Date"):
        super().__init__(mesaage)