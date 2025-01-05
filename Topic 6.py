# Topic 6: Implement a tree to represent hierarchical data in the inventory management system for small pharmacies
# Tree Node Class for Hierarchical Data (Categories and Medicines)
class TreeNode:
    def __init__(self, name, quantity=None, price=None):
        self.name = name          # Name of the medicine or category
        self.quantity = quantity  # Quantity of the medicine (optional for categories)
        self.price = price        # Price of the medicine (optional for categories)
        self.children = []        # List of child nodes (subcategories or medicines)

# Tree Class for managing the hierarchical structure
class MedicineTree:
    def __init__(self):
        self.root = None  # The root of the tree will be the top-level category

    # Add a new category or medicine
    def add(self, parent_name, name, quantity=None, price=None):
        parent_node = self.search(self.root, parent_name)
        if parent_node:
            new_node = TreeNode(name, quantity, price)
            parent_node.children.append(new_node)
            print(f"Added '{name}' under '{parent_name}'.")
        else:
            print(f"Error: Category '{parent_name}' not found.")

    # Search for a node in the tree by name
    def search(self, node, name):
        if not node:
            return None
        if node.name == name:
            return node
        for child in node.children:
            result = self.search(child, name)
            if result:
                return result
        return None

    # Display the tree structure (recursive)
    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("  " * level + f"{node.name} (Quantity: {node.quantity}, Price: ${node.price if node.price else 'N/A'})")
        for child in node.children:
            self.display(child, level + 1)

    # Initialize the root node of the tree (Top-level category)
    def initialize_root(self, name):
        self.root = TreeNode(name)

# Functions for the CLI Interface
def display_inventory(medicine_tree):
    print("\n--- Inventory Hierarchy ---")
    if medicine_tree.root:
        medicine_tree.display(medicine_tree.root)
    else:
        print("Inventory is empty.")

def add_category_or_medicine(medicine_tree):
    parent_name = input("\nEnter the parent category or 'root' for top-level: ").strip()
    name = input("Enter name of the new category or medicine: ").strip()
    if parent_name.lower() == 'root':
        medicine_tree.initialize_root(name)
        print(f"Root category '{name}' initialized.")
    else:
        quantity = int(input("Enter quantity (0 if category): "))
        price = None
        if quantity > 0:
            price = float(input("Enter price: $"))
        medicine_tree.add(parent_name, name, quantity, price)

def main():
    medicine_tree = MedicineTree()  

    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Category or Medicine")
        print("2. Display Inventory Hierarchy")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_category_or_medicine(medicine_tree)
        elif choice == '2':
            display_inventory(medicine_tree)
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
