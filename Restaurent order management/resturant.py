from menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.employees = {}
        self.customers = []

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def show_employees(self):
        for emp in self.employees.values():
            emp.display_info()

