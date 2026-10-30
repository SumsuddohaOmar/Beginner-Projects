from user import Person
from utils import _key
from order import Order

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

    def remove_order(self, item_name):
        for cart_item in self.cart.items:
            if _key(cart_item.name) == _key(item_name):
                self.cart.remove_item_from_cart(cart_item)
                return
        print(f"{cart_item.name} not added in cart.")

    def view_cart(self):
        if self.cart.items:
            print(f"{'Name':<15}{'Price':<8}{'Quantity':<8}")
        else:
            print("Cart is empty.")
        for item, quantity in self.cart.items.items():
            print(f"{item.name:<15}{item.price:<8}{quantity:<8}")

        print(f"Total Bill : {self.cart.total_price}")

    def pay_bill(self, given_bill, menu):
        if not self.cart.items:
            print(f"Cart is empty.")
            return
        else:
            cart_problem = []
            for ord_item in self.cart.items:
                menu_item = menu.search_item(ord_item.name)
                current = self.cart.items.get(ord_item, 0)
                if menu_item is None or menu_item is not ord_item:
                    cart_problem.append((ord_item.name,"Item changed in menu, Please order again."))
                elif menu_item.quantity < current:
                    cart_problem.append((ord_item.name,f"{ord_item.name} : {menu_item.quantity}pcs left "))
            if not cart_problem:
                if given_bill < self.cart.total_price:
                    print(f"Not enough. Your bill is {self.cart.total_price}.")
                elif given_bill == self.cart.total_price:
                    print(f"Bill paid. Thank you.")
                    self.cart.updating_cart_quantity()
                    self.cart.clear_cart()
                elif given_bill > self.cart.total_price:
                    print(
                        f"Bill paid. {given_bill - self.cart.total_price}, here is your change. Thank You."
                    )
                    self.cart.updating_cart_quantity()
                    self.cart.clear_cart()
            else:
                for name,reason in cart_problem:
                    self.remove_order(name)
                    print(reason)
                return