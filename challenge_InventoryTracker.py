#challenge_InventoryTracker.py



from collections import UserDict


class Inventory(UserDict):
    def __init__(self):
        super().__init__()

    def __setitem__(self, item, value):
        #check that key is string
        if not isinstance(item, str):
            raise TypeError(f"Items must be strings, not {type(item).__name__}")
        if not isinstance(value, int):
            raise TypeError(f"Values must be integers, not {type(value).__name__}")
        #if we get here we have the correct types
        #set to lowercase
        super().__setitem__(item.lower(), value)

    def __getitem__(self, item):
        return  super().__getitem__(item).lower()
    
    def __delitem__(self, item):
        return super().__delitem__(item.lower())
    
    def __contains__(self, item):
        return super().__contains__(item.lower())
    
    def update_stock(self, item, addqty):
        if item in self:
            super().value += addqty
        else:
            self[item]=addqty



inv = Inventory()
inv.__setitem__('salt', 89)
inv.__setitem__('Pepper', 95)

print(inv.__contains__('Pepper'))
