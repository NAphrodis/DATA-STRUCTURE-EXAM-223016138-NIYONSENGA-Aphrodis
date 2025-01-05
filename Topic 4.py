# Topic 4: Create Doubly Linked List to manage a fixed number of orders in the inventory management system for small pharmacies
from datetime import datetime


class Order:
    def __init__(self, order_id, medicine_name, quantity, price, order_date):
        self.order_id = order_id  
        self.medicine_name = medicine_name 
        self.quantity = quantity  
        self.price = price  
        self.order_date = order_date  
        self.next = None 
        self.prev = None 

    def __str__(self):
        return f"Order ID: {self.order_id}, Medicine: {self.medicine_name}, Quantity: {self.quantity}, Price: ${self.price}, Order Date: {self.order_date.strftime('%Y-%m-%d')}"


class DoublyLinkedList:
    def __init__(self, max_orders=5):
        self.head = None  
        self.tail = None  
        self.size = 0  
        self.max_orders = max_orders  

   
    def add_order(self, order_id, medicine_name, quantity, price, order_date):
        if self.size >= self.max_orders:
            print("Cannot add more orders. The inventory is full.")
            return

        new_order = Order(order_id, medicine_name, quantity, price, order_date)

        if not self.head: 
            self.head = new_order
            self.tail = new_order
        else:  
            self.tail.next = new_order
            new_order.prev = self.tail
            self.tail = new_order

        self.size += 1
        print(f"Added: {new_order}")

   
    def remove_order(self, order_id):
        current = self.head
        while current:
            if current.order_id == order_id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  
                    self.head = current.next
                if current == self.tail: 
                    self.tail = current.prev
                self.size -= 1
                print(f"Removed order: {current}")
                return
            current = current.next
        print(f"Order ID {order_id} not found.")

    def display_orders(self):
        if self.size == 0:
            print("No orders in the inventory.")
            return
        current = self.head
        print("\n--- Orders ---")
        while current:
            print(current)
            current = current.next


def main():
    max_orders = 5 
    dll = DoublyLinkedList(max_orders)  

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Order")
        print("2. Remove Order")
        print("3. Display Orders")
        print("4. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            if dll.size < dll.max_orders:
                order_id = input("Enter Order ID: ").strip()
                medicine_name = input("Enter Medicine Name: ").strip()
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price per Unit: $"))
                order_date = input("Enter Order Date (YYYY-MM-DD): ").strip()
                order_date = datetime.strptime(order_date, "%Y-%m-%d")
                dll.add_order(order_id, medicine_name, quantity, price, order_date)
            else:
                print("Cannot add more orders. Maximum limit reached.")
                
        elif choice == '2':
            order_id = input("Enter Order ID to remove: ").strip()
            dll.remove_order(order_id)

        elif choice == '3':
            dll.display_orders()

        elif choice == '4':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
