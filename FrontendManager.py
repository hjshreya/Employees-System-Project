from employeemanager import EmployeesManager
from utility import input_is_valid


class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("\nProgram Options:")
        options = [
            "1) Add a new employee",
            "2) List all employees",
            "3) Delete employees by age range",
            "4) Update employee salary by name",
            "5) Exit the program"
        ]
        for option in options:
            print(option)
        return input_is_valid("Enter your choice (1–5): ", 1, len(options))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()

            elif choice == 2:
                self.employees_manager.list_employees()

            elif choice == 3:
                age_from = input_is_valid("Enter starting age: ", 0)
                age_to = input_is_valid("Enter ending age: ", age_from)
                self.employees_manager.delete_employees_within_age_range(age_from, age_to)

            elif choice == 4:
                name = input("Enter employee name: ").strip()
                new_salary = float(input_is_valid("Enter new salary: ", 1))
                self.employees_manager.update_salary_by_name(name, new_salary)

            elif choice == 5:
                print("Exiting the program.")
                break
