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

    def order_item(self, item_name, menu, quantity):
        item = menu.search_item(item_name)
        if item:
            if quantity > 0:
                self.cart.add_item_to_cart(item, quantity)
            else:
                print("Invalid Quantity.")
        else:
            print("Item not found.")
            
    def remove_order(self,item_name, menu):
        item = menu.search_item(item_name)
        if item:
            if item in self.cart.items:
                self.cart.remove_item_from_cart(item)
            else:
                print(f"{item.name} not added in cart.")

    def view_cart(self):
        if self.cart.items:
            print(f"{'Name':<15}{'Price':<8}{'Quantity':<8}")
        else:
            print("Cart is empty.")
        for item, quantity in self.cart.items.items():
            print(f"{item.name:<15}{item.price:<8}{quantity:<8}")
        
        print(f"Total Bill : {self.cart.total_price}")
    
    def pay_bill(self, given_bill, menu):
        for ord_item in self.cart.items:
            ord_item = menu.search_item(ord_item.name)
            if ord_item is None:
                break
        if ord_item:
            if given_bill < self.cart.total_price:
                print(f"Not enough. Your bill is {self.cart.total_price}.")
            elif given_bill == self.cart.total_price:
                print(f"Bill paid. Thank you.")
                self.cart.updating_cart_quantity(ord_item)
                self.cart.clear_cart()
            elif given_bill > self.cart.total_price:
                print(f"Bill paid. {given_bill - self.cart.total_price}, here is your change. Thank You.")
                self.cart.updating_cart_quantity(ord_item)
                self.cart.clear_cart()
        else:
            print("There is subtle change in menu, Please order again.")

class Order:
    def __init__(self):
        self.items = {}

    def add_item_to_cart(self, item, quantity):
        current = self.items.get(item,0)
        if current + quantity <= item.quantity:
            if item in self.items:
                self.items[item] += quantity
                print(f"{quantity}pcs {item.name} added to cart.")
            else:
                self.items[item] = quantity
                print(f"{quantity}pcs {item.name} added to cart.")
        else:
            print(
                f"We have only {item.quantity - current}pcs stock for {item.name}. Sorry for the inconvience"
            )
    def remove_item_from_cart(self,item):
        if item in self.items:
            del self.items[item]
            print(f"{item.name} removed from cart.")
        else:
            print(f"{item.name} not added in cart.")
             
    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def updating_cart_quantity(self, item):
        for item in self.items:
            current = self.items.get(item,0)
            if current <= item.quantity:
                item.quantity -= current
    
    def clear_cart(self):
        self.items = {}

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

    def search_item(self, item_name):
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
customer1.order_item("burger", res1.menu, 20)
customer1.order_item("burger", res1.menu, 7)
customer1.order_item("cola", res1.menu, 4)
customer1.order_item("burger", res1.menu, 3)
customer1.order_item("burger", res1.menu, 1)


customer1.view_cart()
customer1.pay_bill(270,res1.menu)
customer1.view_cart()
res1.menu.show_items()