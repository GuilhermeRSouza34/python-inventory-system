from openpyxl import load_workbook
from excel_utils import load_inventory, save_inventory

class InventoryManager:
    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.stock = self.load_inventory()

    def load_inventory(self):
        return load_inventory(self.excel_file)

    def save_inventory(self):
        save_inventory(self.excel_file, self.stock)

    def add_product(self, product_name, quantity):
        if product_name in self.stock:
            self.stock[product_name] += quantity
        else:
            self.stock[product_name] = quantity
        self.save_inventory()

    def process_request(self, product_name, quantity):
        if product_name in self.stock and self.stock[product_name] >= quantity:
            self.stock[product_name] -= quantity
            self.save_inventory()
            return True
        return False

    def display_inventory(self):
        return self.stock