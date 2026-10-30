from user import Person

class Employee(Person):

    new_emp_id = 1

    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.emp_id = Employee.new_emp_id
        Employee.new_emp_id += 1
        self.age = age
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Designation : {self.designation}")
        print(f"Salary : {self.salary}")
        print(f"Phone : {self.phone}")
        print(f"Email : {self.email}\n")
