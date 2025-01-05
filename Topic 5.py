# Topic 5: Use Heap to track data dynamically in inventory management system for small pharmacies
import heapq
from datetime import datetime


class Medicine:
    def __init__(self, name, quantity, price, expiry_date):
        self.name = name  
        self.quantity = quantity 
        self.price = price  
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")  
        self.date_added = datetime.now() 

    def __lt__(self, other):
       
        return self.price < other.price

    def __str__(self):
        return f"Medicine: {self.name}, Price: ${self.price}, Quantity: {self.quantity}, Expiry: {self.expiry_date.strftime('%Y-%m-%d')}, Added: {self.date_added.strftime('%Y-%m-%d')}"


class Inventory:
    def __init__(self):
        self.heap = []  
        self.size = 0 

    
    def add_medicine(self, name, quantity, price, expiry_date):
        medicine = Medicine(name, quantity, price, expiry_date)
        heapq.heappush(self.heap, medicine)  
        self.size += 1
        print(f"Added: {medicine}")

   
    def remove_medicine(self):
        if self.size == 0:
            print("No medicines in the inventory.")
            return
        removed_medicine = heapq.heappop(self.heap)  
        self.size -= 1
        print(f"Removed: {removed_medicine}")

    
    def display_medicines(self):
        if self.size == 0:
            print("No medicines in the inventory.")
            return
        print("\n--- Medicines in Inventory ---")
       
        for medicine in sorted(self.heap, key=lambda x: x.price):
            print(medicine)

    
    def update_medicine(self, name, new_price=None, new_quantity=None):
        for i, medicine in enumerate(self.heap):
            if medicine.name == name:
              
                if new_price is not None:
                    medicine.price = new_price
                    print(f"Updated {name} price to ${new_price}")
                
                
                if new_quantity is not None:
                    medicine.quantity = new_quantity
                    print(f"Updated {name} quantity to {new_quantity}")

                heapq.heapify(self.heap)  
                return
        print(f"Medicine {name} not found in inventory.")

def main():
    inventory = Inventory() 

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Medicine")
        print("2. Remove Medicine (Lowest Price)")
        print("3. Update Medicine (Price or Quantity)")
        print("4. Display Medicines")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter medicine name: ").strip()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: $"))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ").strip()
            inventory.add_medicine(name, quantity, price, expiry_date)

        elif choice == '2':
            inventory.remove_medicine()

        elif choice == '3':
            name = input("Enter medicine name to update: ").strip()
            update_choice = input("Do you want to update (P)rice, (Q)uantity, or (B)oth? ").strip().upper()

            if update_choice == 'P':
                new_price = float(input("Enter the new price: $"))
                inventory.update_medicine(name, new_price=new_price)
            elif update_choice == 'Q':
                new_quantity = int(input("Enter the new quantity: "))
                inventory.update_medicine(name, new_quantity=new_quantity)
            elif update_choice == 'B':
                new_price = float(input("Enter the new price: $"))
                new_quantity = int(input("Enter the new quantity: "))
                inventory.update_medicine(name, new_price=new_price, new_quantity=new_quantity)
            else:
                print("Invalid option. Please try again.")

        elif choice == '4':
            inventory.display_medicines()

        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
