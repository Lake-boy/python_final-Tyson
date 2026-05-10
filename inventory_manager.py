
import list

class InventoryManager:
    def __init__(self):
        #Products
        self.products = list.products
    
    def add_products(self):
        product_id = input().lower().strip()
        product_name = input().lower().strip()
        category = input().lower().strip()
        quantity = int(input().strip())
        reorder_level = input().lower().strip()
        reorder_quantity = input().lower().strip()
        unit_price = input().lower().strip()
        vendor_id = input().lower().strip()
        active_status = True

        self.products = {product_name : {"product_id" : product_id,
        "product_name" : product_name, "category" : category, "quantity" : quantity,
        "reorder_level" : reorder_level, "reorder_quantity" : reorder_quantity,
        "unit_price" : unit_price, "vendor_id" : vendor_id, "active_status" : active_status
        }}

    def view_products(self):
        for product in self.products:
            if self.products[product]["quantity"] <= 100:
                print(f"Name:{product} ID:{self.products[product]["product_id"]} Stock is low")
            else:
                print(f"Name:{product} ID:{self.products[product]["product_id"]}")

    def edit_product(self):
        product_name = input("Product name ->").lower().strip()
        product_edit = input("\n EX: product_id, quantity, reorder_quantity, product_name, reorder_level," \
        "unit_price, vendor_id, active_status. \n" \
        "What you want to edit ->").lower().strip()

        if product_edit == "product_name":
            userinput = input().lower().strip()
            self.products[product_name] = userinput
            self.products[userinput][product_name] = userinput
        elif product_edit == "active_status" and self.products[product_name][product_edit] == True:
            userinput = ("Turn the product off? EX: Y/N -> ").lower().strip()
            if userinput == "y":
                self.products[product_name][product_edit] = False
            elif userinput == "n":
                self.products[product_name][product_edit] = True
        elif product_edit == "active_status" and self.products[product_name][product_edit] == True:
            userinput = ("Turn the product on? EX: Y/N -> ").lower().strip()
            if userinput == "y":
                self.products[product_name][product_edit] = True
            elif userinput == "n":
                self.products[product_name][product_edit] = False
        else:
            userinput = input().lower().strip()
            self.products[product_name][product_edit] = userinput
