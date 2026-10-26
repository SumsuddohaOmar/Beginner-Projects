from abc import ABC, abstractmethod


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
        self.new_emp_id = Employee.new_emp_id
        Employee.new_emp_id += 1
        self.age = age
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print(f"Name : {self.name}")


class Customer(Person):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def display_info(self):
        pass


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
            if item_name in self.items:
                self.items[item_name].quantity += adding_quantity
                print("Item Quantity Updated Successfully.")
            else:
                print("Item doesn't exist.")
        else:
            print("Invalid Quantity.")

    def add_item(self, item):
        if item.name not in self.items:
            self.items[item.name] = item
            print("Item Added Successfully.")
        else:
            print(
                "Item Already Exist. Either rename the item name or add the quantity existing name"
            )

    def delete_item(self, del_item):
        if del_item in self.items:
            del self.items[del_item]
            print("Item Removed Successfully.")
        else:
            print("Item Doesn't Exist.")

    def show_items(self):
        for item in self.items.values():
            print(f"Name : {item.name}")
            print(f"Price : {item.price}")
            print(f"Quantity : {item.quantity}\n")


# menu = Menu()
# menu.add_item(Item("Burger", 25, 10))
# menu.add_item(Item("Burger", 25, 10))
# menu.add_item(Item("Cola", 5, 50))

# menu.add_item_quantity("Burger", 5)
# menu.add_item_quantity("Pizza", 5)
# menu.add_item_quantity("Cola", -3)
# menu.show_items()
# menu.delete_item("Cola")
# menu.show_items()
