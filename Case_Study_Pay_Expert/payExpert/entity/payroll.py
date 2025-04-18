class Payroll:
    def __init__(self, payroll_id, employee_id, start_date, end_date, basic_salary, overtime_pay, deductions, net_salary):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.start_date = start_date
        self.end_date = end_date
        self.basic_salary = basic_salary
        self.overtime_pay = overtime_pay
        self.deductions = deductions
        self.net_salary = net_salary

    def __str__(self):
        return f"Payroll for Employee {self.employee_id} - Net Salary: {self.net_salary}"
