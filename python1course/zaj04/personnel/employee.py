class Employee:
    __max_id = 0

    def __init__(self, first_name: str, last_name: str, salary: float):
        self.employee_id = self.get_next_id()
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def get_next_id(cls):
        cls.__max_id += 1
        return cls.__max_id

    @classmethod
    def reset_id_counter(cls):
        cls.__max_id = 0

    def display_info(self):
        print(
            f"Employee ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}"
        )

    def update_salary(self, new_salary: float):
        self.salary = new_salary
        print(f"Updated salary: {new_salary}")

    def __str__(self):
        return f"Employee({self.first_name} {self.last_name}, ID: {self.employee_id})"

    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.employee_id}, {self.salary})"
