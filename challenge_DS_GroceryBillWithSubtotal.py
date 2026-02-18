#challenge_DS_GroceryBillWithSubtotal


from collections import Counter

Price = {"Soap": 50, "Toothpaste": 25, "Shampoo" : 45.50, "Toothbrush":15.99}


def generate_bill(cart):
    #abdul iterated through cart which is more correct.  I changed it....
    total = 0
    print('\nProduct          Price         Qty  Sub-Total')
    for k, v in cart.items():
        qty = v
        price = Price[k]
        val = qty * price
        total += val
        if k == 'Soap':
            print(f'{k} \t\t: {price}\tX\t{qty} =  {val}  ')
        else:
             print(f'{k} \t: {price}\tX \t{qty} =  {val}  ')
        
    print(f'\t\t\t    Total = {total}')


if __name__ == "__main__":
    Cart = Counter({"Soap": 5, "Toothpaste": 1, "Shampoo" : 2, "Toothbrush": 3})
    generate_bill(Cart)
