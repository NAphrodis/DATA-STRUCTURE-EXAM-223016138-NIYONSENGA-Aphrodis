# Topic 7: Use Bubble Sort to sort the inventory management system for small pharmacies data based on priority
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

    
    def bubble_sort_by_expiry(self):
        n = len(self.medicines)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.medicines[j].expiry_date > self.medicines[j+1].expiry_date:

                    self.medicines[j], self.medicines[j+1] = self.medicines[j+1], self.medicines[j]
        print("Sorted medicines by expiry date.")

  
    def bubble_sort_by_addition_date(self):
        n = len(self.medicines)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.medicines[j].date_added > self.medicines[j+1].date_added:
                   
                    self.medicines[j], self.medicines[j+1] = self.medicines[j+1], self.medicines[j]
        print("Sorted medicines by date of addition.")

  
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
        print("2. Display Inventory")
        print("3. Sort Inventory by Expiry Date (priority)")
        print("4. Sort Inventory by Date of Addition (priority)")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter medicine name: ").strip()
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: $"))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ").strip() 
            inventory.add_medicine(name, quantity, price, expiry_date)
        elif choice == '2':
            inventory.display_inventory()
        elif choice == '3':
            inventory.bubble_sort_by_expiry()
            inventory.display_inventory()  
        elif choice == '4':
            inventory.bubble_sort_by_addition_date()
            inventory.display_inventory()  
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
