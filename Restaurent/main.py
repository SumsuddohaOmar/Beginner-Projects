from employee import Employee
from utils import _key
from customer import Customer
from order import Item
from menu import Menu
from resturant import Restaurant


def customer_menu(restaurant):
    print("\n--- Create Account ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    customer = Customer(name, phone, email, address)
    restaurant.customers.append(customer)
    print(f"Welcome, {customer.name}!")

    while True:
        print("\n--- Customer Menu ---")
        print("1. View menu")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. View cart")
        print("5. Pay bill")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            restaurant.menu.show_items()
        elif choice == "2":
            item_name = input("Item name: ")
            quantity = int(input("Quantity: "))
            customer.order_item(item_name, restaurant.menu, quantity)
        elif choice == "3":
            customer.remove_order(input("Item name: "))
        elif choice == "4":
            customer.view_cart()
        elif choice == "5":
            customer.view_cart()
            given_bill = int(input("Amount given: "))
            customer.pay_bill(given_bill, restaurant.menu)
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def admin_menu(restaurant):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add item")
        print("2. View items")
        print("3. Delete item")
        print("4. Add employee")
        print("5. View employees")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Item name: ")
            price = int(input("Price: "))
            quantity = int(input("Quantity: "))
            restaurant.menu.add_item(Item(name, price, quantity))
        elif choice == "2":
            restaurant.menu.show_items()
        elif choice == "3":
            restaurant.menu.delete_item(input("Item name: "))
        elif choice == "4":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            age = int(input("Age: "))
            designation = input("Designation: ")
            salary = int(input("Salary: "))
            restaurant.add_employee(
                Employee(name, phone, email, address, age, designation, salary)
            )
        elif choice == "5":
            restaurant.show_employees()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


def main():
    restaurant = Restaurant("Star")
    while True:
        print("\n=== Restaurant Management System ===")
        print("1. Customer")
        print("2. Admin")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            customer_menu(restaurant)
        elif choice == "2":
            admin_menu(restaurant)
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


main()
