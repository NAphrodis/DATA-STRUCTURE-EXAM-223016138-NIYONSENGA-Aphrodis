# Topic 3: Implement Array for inventory management system for small pharmacies processing

from datetime import datetime

class Medicine:
    def __init__(self, name, quantity, price, expiry_date):
        self.name = name              
        self.quantity = quantity      
        self.price = price            
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d") 
        self.date_added = datetime.now()  

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price}, Expiry: {self.expiry_date.strftime('%Y-%m-%d')}, Added: {self.date_added.strftime('%Y-%m-%d')})"

class Inventory:
    def __init__(self):
        self.medicines = []  

   
    def add_medicine(self, name, quantity, price, expiry_date):
        medicine = Medicine(name, quantity, price, expiry_date)
        self.medicines.append(medicine)  
        print(f"Added {medicine}")

    
    def update_medicine(self, name, new_quantity=None, new_price=None):
        for medicine in self.medicines:
            if medicine.name.lower() == name.lower():  
                if new_quantity is not None:
                    medicine.quantity = new_quantity
                if new_price is not None:
                    medicine.price = new_price
                print(f"Updated {medicine}")
                return
        print(f"Medicine {name} not found in inventory.")

    
    def remove_medicine(self, name):
        for medicine in self.medicines:
            if medicine.name.lower() == name.lower():  
                self.medicines.remove(medicine)
                print(f"Removed {medicine.name} from inventory.")
                return
        print(f"Medicine {name} not found in inventory.")

  
    def display_inventory(self):
        if not self.medicines:
            print("Inventory is empty.")
            return
        print("\n--- Inventory ---")
        for medicine in self.medicines:
            print(medicine)

def main():
    inventory = Inventory()  

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Medicine")
        print("2. Update Medicine")
        print("3. Remove Medicine")
        print("4. Display Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter medicine name: ").strip()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: $"))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ").strip()  
            inventory.add_medicine(name, quantity, price, expiry_date)
        elif choice == '2':
            name = input("Enter the medicine name to update: ").strip()
            new_quantity = input("Enter new quantity (leave blank to keep current): ").strip()
            new_price = input("Enter new price (leave blank to keep current): ").strip()
            
            new_quantity = int(new_quantity) if new_quantity else None
            new_price = float(new_price) if new_price else None
            inventory.update_medicine(name, new_quantity, new_price)
        elif choice == '3':
            name = input("Enter the medicine name to remove: ").strip()
            inventory.remove_medicine(name)
        elif choice == '4':
            inventory.display_inventory()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
