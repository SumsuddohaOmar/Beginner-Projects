from abc import ABC, abstractmethod

def _key(name):
    return name.lower().strip()


class Person(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    @abstractmethod
    def display_info(self):
        pass


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


class Customer(Person):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        
    def display_info(self):
        pass
    
    def order_item(self,item_name, menu, quantity):
        item = menu.search_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item_to_cart(item)
            print("Item added to cart.")
        else:
            print("Item not found.")
            
    def view_cart(self):
        if self.cart:
            print(f"{'Name':<15}{'Price':<8}{'Quantity':<8}")
        else:
            print("Menu is empty.")
        for item,quantity in self.cart.items.items():
            print(f"{item.name:<15}{item.price:<8}{quantity:<8}")
            
class Order:
    def __init__(self):
        self.items = {}
    
    def add_item_to_cart(self, item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price


class Menu:
    def __init__(self):
        self.items = {}

    def add_item_quantity(self, item_name, adding_quantity):
        if adding_quantity > 0:
            key = _key(item_name)
            if key in self.items:
                self.items[key].quantity += adding_quantity
                print("Item Quantity Updated Successfully.")
            else:
                print("Item doesn't exist.")
        else:
            print("Invalid Quantity.")
        
    def search_item(self,item_name):
        key = _key(item_name)
        if key in self.items:
            return self.items[key]
        else:
            return None
            
# for adding item

    def add_item(self, item):
        key = _key(item.name)
        if key not in self.items:
            self.items[key] = item
            print("Item Added Successfully.")
        else:
            print(
                "Item Already Exist. Either rename the item name or add the quantity existing name"
            )
            
# for deleting item

    def delete_item(self, del_item):
        key = _key(del_item)
        if key in self.items:
            del self.items[key]
            print("Item Removed Successfully.")
        else:
            print("Item Doesn't Exist.")

    def show_items(self):
        if self.items:
            print(f"{'Name':<15}{'Price':<8}{'Quantity':<8}")
        else:
            print("Menu is empty.")
        for item in self.items.values():
            print(f"{item.name:<15}{item.price:<8}{item.quantity:<8}")

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

res1 = Restaurant("Star")
res1.menu.add_item(Item("Burger", 25, 10))
res1.menu.add_item(Item("Burger", 25, 10))
res1.menu.add_item(Item("Cola", 5, 50))

# res1.menu.add_item_quantity("Burger", 5)
# res1.menu.add_item_quantity("Pizza", 5)
# res1.menu.add_item_quantity("Cola", -3)
# res1.menu.show_items()
# res1.menu.delete_item("cola")
res1.menu.show_items()

# res1.add_employee(Employee("Omar","156465","omar@gmail.com", "saudi", 26, "waiter", 1000))
# res1.add_employee(Employee("Ahmed Khan", "0501234567", "ahmed@star.com", "Riyadh", 30, "Chef", 6000))
# res1.add_employee(Employee("Sara Ali", "0559876543", "sara@star.com", "Jeddah", 26, "Cashier", 4500))

# res1.show_employees()
customer1 = Customer("Ahmed Khan", "0501234567", "ahmed@star.com", "Riyadh")
customer1.order_item('burger',res1.menu,2)
customer1.view_cart()
res1.menu.show_items()