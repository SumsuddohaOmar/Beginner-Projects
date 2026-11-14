from menu import Menu
from db import get_conn
conn = get_conn()

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu(conn)
        self.employees = {}
        self.customers = []

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def show_employees(self):
        for emp in self.employees.values():
            emp.display_info()

