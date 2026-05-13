
class InventoryManager:
    def __init__(self):
        self.products = {}
    
    def add_products(self):
        while True:
            product_id = input("Whats the Product ID -> ").lower().strip()

            # Verifies product ID's in the  worst way possible. Maybe I dont't know it's all I could think of.
            products_looked_at = 0
            product_unique_ids = 0

            for product in self.products:
                products_looked_at += 1
                product_unique_ids += 1 

                if self.products[product]["product_id"] == product_id:
                    print("duplicate product ID")
                    product_unique_ids -= 1
                
            if product_unique_ids == products_looked_at:
                break

        product_name = input("Whats the Product name -> ").lower().strip()

        category = input("Whats the Product category ->").lower().strip()

        quantity = input("Whats the Product quantity -> ").strip()

        reorder_level = input("Whats the reorder level -> ").lower().strip()

        reorder_quantity = input("Whats the reorder quantity ->").lower().strip()

        unit_price = input("Whats the unit price").lower().strip()

        vendor_id = input("Whats the vendors ID").lower().strip()

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
    
    def search_product(self):
        search_by = input("\n EX: product_id, reorder_quantity, category, vendor_id,\n"
            "Search by -> ").lower().strip()
        search = input("\n Search -> ")

        for product in self.products:
            if self.products[product][search_by] == search:
                print(
                    f"\n Name: {self.products[product]} ID: {self.products[product]["product_id"]} Vendor ID: {self.products[product]["vendor_id"]}\n"
                    f" Is Active: {self.products[product]["active_status"]} Price: ${self.products[product]["unit_price"]} Quantity: {self.products[product]["quantity"]}\n"
                    f" Reorder Level: {self.products[product]["reorder_level"]} Reorder Quantiy: {self.products[product]["reorder_quantity"]} Category: {self.products[product]["category"]}"
                )


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
        elif product_edit == "active_status" and self.products[product_name][product_edit] == False:
            userinput = ("Turn the product on? EX: Y/N -> ").lower().strip()
            if userinput == "y":
                self.products[product_name][product_edit] = True
            elif userinput == "n":
                self.products[product_name][product_edit] = False
        else:
            userinput = input().lower().strip()
            self.products[product_name][product_edit] = userinput
