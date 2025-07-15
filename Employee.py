class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary  # private

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary must be positive")

    def __str__(self):
        return f'Employee {self.name} has age {self.age} and salary {self.__salary}'

