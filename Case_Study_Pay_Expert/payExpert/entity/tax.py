
class Tax:
    def __init__(self, tax_id, employee_id, tax_year, taxable_income, tax_amount):
        self.tax_id = tax_id
        self.employee_id = employee_id
        self.tax_year = tax_year
        self.taxable_income = taxable_income
        self.tax_amount = tax_amount

    def __str__(self):
        return (f"TaxID: {self.tax_id}, EmployeeID: {self.employee_id}, "
                f"Year: {self.tax_year}, Taxable Income: ₹{self.taxable_income}, "
                f"Tax Amount: ₹{self.tax_amount}")
