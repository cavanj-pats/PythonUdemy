#challenge_PaymentMethod.py



class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

class Crypto(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Crypto.")


def process_payment(paymethod, amount):
    paymethod.pay(amount)



if __name__ == "__main__":
    #abdul used a for loop to test all different payment types.
    payments = [CreditCard(),
                PayPal(),
                Crypto()]
    
    for method in payments:

        process_payment(method, 20)
