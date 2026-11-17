from utils import _key
from order import Item
import mysql.connector
class Menu:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()
    
    def add_item_quantity(self, item_name, adding_quantity):
        if adding_quantity > 0:
            key = _key(item_name)
            self.cursor.execute(
                "UPDATE menu SET quantity = quantity + %s WHERE name = %s",
                (adding_quantity,key)
            )
            self.conn.commit()
            if self.cursor.rowcount > 0:
                print("Item Quantity Updated Successfully.")
            else:   
                print("Item doesn't exist.")
        else:
            print("Invalid Quantity.")

    def search_item(self, item_name):
        key = _key(item_name)
        self.cursor.execute(
            "SELECT name, price, quantity FROM menu WHERE name = %s", (key,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        else:
            return Item(row[0],row[1],row[2])
        
    # for adding item

    def add_item(self, item):
        key = _key(item.name)
        try:
            self.cursor.execute(
                "INSERT INTO menu(name,price,quantity) VALUES(%s,%s,%s)",
                (key,item.price,item.quantity)
            )
            self.conn.commit()
            print("Item Added Successfully.")
        except mysql.connector.IntegrityError:
            print(
                "Item Already Exist. Either rename the item name or add the quantity existing name"
            )

    # for deleting item

    def delete_item(self, del_item):
        key = _key(del_item)
        self.cursor.execute(
            "DELETE FROM menu WHERE name = %s",
            (key,)
        )
        self.conn.commit()
        if self.cursor.rowcount > 0:
            print("Item Removed Successfully.")
        else:
            print("Item Doesn't Exist.")

    def show_items(self):
        self.cursor.execute("SELECT name, price, quantity FROM menu")
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            print(f"{"Item name":<15}{"Price":<8}{"Quantity"}")
            print(f"{"-"*9:<15}{"-"*5:<8}{"-"*8}")
            for row in rows:
                print(f"{row[0]:<15}{row[1]:<8}{row[2]}")
        else:
            print("Menu is empty.")