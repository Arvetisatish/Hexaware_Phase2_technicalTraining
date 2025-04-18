class Employee:
    def __init__(self, employee_id, first_name, last_name, dob, gender, email, phone, address, position, joining_date, termination_date=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.address = address
        self.position = position
        self.joining_date = joining_date
        self.termination_date = termination_date

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"
