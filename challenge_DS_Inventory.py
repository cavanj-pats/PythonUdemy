#challenge_DS_Inventory.py

from collections import Counter

inventory = Counter({"apple": 50, "mango":100, "banana": 120, "orange": 70})



def update_inventory(order):
    inventory.subtract(order)

if __name__ == "__main__":
    print(inventory)
    order = Counter({"apple": 10, "mango": 12, "banana": 15, "orange": 5})
    update_inventory(order)
    print(inventory)
