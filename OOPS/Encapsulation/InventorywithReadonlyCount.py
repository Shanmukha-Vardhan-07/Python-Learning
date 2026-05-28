class Inventory:
    def __init__(self):
        self._items=[]

    def add_item(self,item):
        self._items.append(item)
        print(f"{item} is added succesfully")

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
            print(f"{item} is removed succesfully")
        else:
            print(f"{item} Not found")

    def count(self):
        return len(self._items)
    
inventory = Inventory()

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Show Item Count")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ")
        inventory.add_item(item)

    elif choice == "2":
        item = input("Enter item name: ")
        inventory.remove_item(item)

    elif choice == "3":
        print("Total Items:", inventory.count())

    elif choice == "4":
        print("Exiting Inventory System...")
        break

    else:
        print("Invalid choice! Try again.")