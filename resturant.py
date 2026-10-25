
class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
        
class Menu:
    def __init__(self):
        self.items = {}
        
    def add_item(self, item):
        self.items[item.name] = item
        
    def delete_item(self, item):
        del self.items[item.name]
        
        
menu = Menu()       
menu.add_item(Item("Burger", 25, 10))
menu.add_item(Item("Cola", 5, 50))

print(menu.items)