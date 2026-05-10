
from inventory_manager import InventoryManager

class Main:
    def __init__(self):

        """file imports"""
        self.inventory = InventoryManager()

    def run_system(self):
        self.inventory.add_products()
        self.inventory.view_products()
        self.inventory.edit_product()

if __name__ == "__main__":
    system = Main()
    system.run_system()