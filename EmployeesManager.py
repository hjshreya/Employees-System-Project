from utility import input_is_valid
from employee import Employee


class EmployeesManager:
    def __init__(self):
        self._employees = []  # Protected attribute

    def add_employee(self):
        print("\nEnter employee details:")
        name = input("Enter employee name: ").strip()
        age = input_is_valid("Enter employee age: ", 18, 100)
        salary = float(input_is_valid("Enter employee salary: ", 1))

        new_employee = Employee(name, age, salary)
        self._employees.append(new_employee)
        print(f"Employee '{name}' added successfully.")

    def list_employees(self):
        if not self._employees:
            print("\nEmployee list is empty.")
            return

        print("\nEmployee Records:")
        for emp in self._employees:
            print(emp)

    def delete_employees_within_age_range(self, age_from: int, age_to: int):
        original_count = len(self._employees)
        self._employees = [
            emp for emp in self._employees
            if not (age_from <= emp.age <= age_to)
        ]
        deleted_count = original_count - len(self._employees)
        print(f"Deleted {deleted_count} employee(s) in age range {age_from} to {age_to}.")

    def find_employee_by_name(self, name: str) -> Employee | None:
        for emp in self._employees:
            if emp.name.lower() == name.lower():
                return emp
        return None

    def update_salary_by_name(self, name: str, new_salary: float):
        emp = self.find_employee_by_name(name)
        if emp:
            emp.set_salary(new_salary)
            print(f"Salary for '{name}' updated to ₹{new_salary}.")
        else:
            print("Error: No employee found with that name.")
