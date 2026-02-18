from .employee import Employee


class Driver(Employee):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        salary: float,
        license_number: str,
        qualifications: list,
    ):
        super().__init__(first_name, last_name, salary)
        self.license_number = license_number
        self.qualifications = qualifications

    def display_info(self):
        qualifications_joined = ", ".join(self.qualifications)
        return f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}, License Number: {self.license_number}, Qualifications: {qualifications_joined}"

    def __str__(self):
        return f"Driver({self.first_name} {self.last_name}, ID: {self.employee_id}, License: {self.license_number})"

    def __repr__(self):
        return f"Driver('{self.first_name}', '{self.last_name}', {self.employee_id}, {self.salary}, '{self.license_number}', {self.qualifications})"
