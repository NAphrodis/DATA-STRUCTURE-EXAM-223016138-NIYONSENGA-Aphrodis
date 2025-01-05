# Topic 2: Implement Binary Search Tree (BST) and Singly Linked List to manage data in the inventory management system for small pharmacies.
class BSTNode:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, name, quantity, price):
        if not self.root:
            self.root = BSTNode(name, quantity, price)
        else:
            self._insert(self.root, name, quantity, price)

    def _insert(self, node, name, quantity, price):
        if name < node.name:
            if node.left:
                self._insert(node.left, name, quantity, price)
            else:
                node.left = BSTNode(name, quantity, price)
        elif name > node.name:
            if node.right:
                self._insert(node.right, name, quantity, price)
            else:
                node.right = BSTNode(name, quantity, price)

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if not node or node.name == name:
            return node
        elif name < node.name:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    def inorder(self):
        medicines = []
        self._inorder(self.root, medicines)
        return medicines

    def _inorder(self, node, medicines):
        if node:
            self._inorder(node.left, medicines)
            medicines.append((node.name, node.quantity, node.price))
            self._inorder(node.right, medicines)

    def update_quantity(self, name, quantity):
        medicine = self.search(name)
        if medicine:
            medicine.quantity += quantity
            return True
        return False


class TransactionNode:
    def __init__(self, transaction_type, name, quantity):
        self.transaction_type = transaction_type
        self.name = name
        self.quantity = quantity
        self.next = None


class TransactionList:
    def __init__(self):
        self.head = None

    def add_transaction(self, transaction_type, name, quantity):
        new_node = TransactionNode(transaction_type, name, quantity)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def get_transactions(self):
        transactions = []
        temp = self.head
        while temp:
            transactions.append((temp.transaction_type, temp.name, temp.quantity))
            temp = temp.next
        return transactions

def display_inventory(bst):
    inventory = bst.inorder()
    if inventory:
        print("\n--- Current Inventory ---")
        for medicine in inventory:
            print(f"Name: {medicine[0]}, Quantity: {medicine[1]}, Price: ${medicine[2]:.2f}")
    else:
        print("\nInventory is empty.")
        
def display_transactions(transactions):
    transaction_list = transactions.get_transactions()
    if transaction_list:
        print("\n--- Transaction History ---")
        for transaction in transaction_list:
            print(f"{transaction[0]}: {transaction[1]}, Quantity: {transaction[2]}")
    else:
        print("\nNo transactions recorded.")
        
def add_medicine(bst):
    name = input("\nEnter medicine name: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: $"))
    bst.insert(name, quantity, price)
    print(f"{name} added to inventory.")

def search_medicine(bst):
    name = input("\nEnter medicine name to search: ").strip()
    result = bst.search(name)
    if result:
        print(f"Medicine found - Name: {result.name}, Quantity: {result.quantity}, Price: ${result.price:.2f}")
    else:
        print(f"Medicine '{name}' not found in inventory.")

def record_transaction(transactions, bst):
    transaction_type = input("\nEnter transaction type (Sale/Restock): ").strip()
    name = input("Enter medicine name: ").strip()
    quantity = int(input("Enter quantity: "))
    
  
    transactions.add_transaction(transaction_type, name, quantity)
    
    if transaction_type.lower() == "sale":
        if bst.update_quantity(name, -quantity):
            print(f"Sold {quantity} of {name}.")
        else:
            print(f"Error: {name} not found or insufficient stock.")
    elif transaction_type.lower() == "restock":
        bst.update_quantity(name, quantity)
        print(f"Restocked {quantity} of {name}.")
    else:
        print("Invalid transaction type. Only 'Sale' or 'Restock' allowed.")


def main():
    bst = BST() 
    transactions = TransactionList() 

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Medicine")
        print("2. Search Medicine")
        print("3. Display Inventory")
        print("4. Record Transaction (Sale/Restock)")
        print("5. Display Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_medicine(bst)
        elif choice == '2':
            search_medicine(bst)
        elif choice == '3':
            display_inventory(bst)
        elif choice == '4':
            record_transaction(transactions, bst)
        elif choice == '5':
            display_transactions(transactions)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
