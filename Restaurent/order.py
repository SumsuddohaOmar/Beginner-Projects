

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.quantity = quantity
        self.price = price

class Order:
    def __init__(self):
        self.items = {}

    def add_item_to_cart(self, item, quantity):
        current = self.items.get(item, 0)
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

    def remove_item_from_cart(self, item):
        if item in self.items:
            del self.items[item]
            print(f"{item.name} removed from cart.")
        else:
            print(f"{item.name} not added in cart.")

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())

    def updating_cart_quantity(self):
        for item in self.items:
            item.quantity -= self.items[item]

    def clear_cart(self):
        self.items = {}
