class Record:
    def __init__(self, item_name, creator):
        self.item_name = item_name
        self.creator = creator
        self.handler = None
        self.seller = None
        self.buyer = None
        self.stage = "Created"

    def transfer(self, handler):
        self.handler = handler
        self.stage = "Transferred"

    def list_for_sale(self, seller):
        self.seller = seller
        self.stage = "Listed for Sale"

    def purchase(self, buyer):
        self.buyer = buyer
        self.stage = "Purchased"

    def display(self):
        print(f"Item:            {self.item_name}")
        print(f"Manufacturer:    {self.creator}")
        print(f"Handler:         {self.handler if self.handler else 'N/A'}")
        print(f"Seller:          {self.seller if self.seller else 'N/A'}")
        print(f"Buyer:           {self.buyer if self.buyer else 'N/A'}")
        print(f"Current Stage:   {self.stage}")
        print("-" * 30)

class SupplyChain:
    def __init__(self):
        self.history = []

    def create_item(self):
        item_name = input("Enter item name: ")
        creator = input("Enter manufacturer name: ")
        record = Record(item_name, creator)
        self.history.append(record)
        print("Item Created:")
        record.display()

    def transfer_item(self):
        item_name = input("Enter item name for transfer: ")
        handler = input("Enter handler name: ")
        for record in self.history:
            if record.stage == "Created" and record.item_name == item_name:
                record.transfer(handler)
                print("Item Transferred:")
                record.display()
                return
        print("Item not found or already transferred.")

    def list_item_for_sale(self):
        item_name = input("Enter item name for sale listing: ")
        seller = input("Enter seller name: ")
        for record in self.history:
            if record.stage == "Transferred" and record.item_name == item_name:
                record.list_for_sale(seller)
                print("Item Listed for Sale:")
                record.display()
                return
        print("Item not found or not yet transferred.")

    def purchase_item(self):
        item_name = input("Enter item name for purchase: ")
        buyer = input("Enter buyer name: ")
        for record in self.history:
            if record.stage == "Listed for Sale" and record.item_name == item_name:
                record.purchase(buyer)
                print("Item Purchased:")
                record.display()
                return
        print("Item not found or not yet listed for sale.")

    def view_history(self):
        print("\n--- Full History ---")
        for record in self.history:
            record.display()


if __name__ == "__main__":
    supply_chain = SupplyChain()

    while True:
        print("\n1. Create Item")
        print("\n2. Transfer Item")
        print("\n3. List Item for Sale")
        print("\n4. Purchase Item")
        print("\n5. View History")
        print("\n6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            supply_chain.create_item()
        elif choice == '2':
            supply_chain.transfer_item()
        elif choice == '3':
            supply_chain.list_item_for_sale()
        elif choice == '4':
            supply_chain.purchase_item()
        elif choice == '5':
            supply_chain.view_history()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
