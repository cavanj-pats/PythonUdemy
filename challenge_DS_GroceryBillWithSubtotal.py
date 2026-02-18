#challenge_DS_GroceryBillWithSubtotal


from collections import Counter

Price = {"Soap": 50, "Toothpaste": 25, "Shampoo" : 45.50, "Toothbrush":15.99}

def generate_bill(cart):

    for k, v in Price.items():
        qty = cart[k]
        val = qty * v
        if k == 'Soap':
            print(f'{k} \t\t: {v}\tX\t{qty} =  {val}  ')
        else:
             print(f'{k} \t: {v}\tX \t{qty} =  {val}  ')
        


if __name__ == "__main__":
    Cart = Counter({"Soap": 5, "Toothpaste": 1, "Shampoo" : 2, "Toothbrush": 3})
    generate_bill(Cart)
