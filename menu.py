from utils import _key

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
