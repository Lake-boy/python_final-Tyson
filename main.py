import sys

from inventory_manager import InventoryManager

class Main:
    def __init__(self):

        """file imports"""
        self.inventory = InventoryManager()

    def run_system(self):

        while True:
            print("1 : Inventory Manager ")
            print("4 : Quit")
            
            user_input = input().strip()

            if user_input =="1":
                while True:
                    print("1 : add_products" \
                    "2 : view_product" \
                    "3 : search_produc" \
                    "4 : edit_product" \
                    "5 : Go Back.")

                    user_input = input().strip()

                    if user_input == "1":
                        self.inventory.add_products()
                    elif user_input == "2":
                        self.inventory.view_products()
                    elif user_input == "3":
                        self.inventory.search_product()
                    elif user_input == "4":
                        self.inventory.edit_product()
                    elif user_input == "5":
                        break
                    else:
                        print("Not valid user input.\n")

            elif user_input =="4":
                sys.exit
            else:
                print("Not valid user input.\n")

if __name__ == "__main__":
    system = Main()
    system.run_system()