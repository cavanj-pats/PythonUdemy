#account withdrawal management with exception handling - challenge


class InsufficientFundsError(Exception):
    pass




def withdraw(balance, amount):
    if (balance >= amount):
        balance -= amount
    else:
        raise InsufficientFundsError
    


balance = 5000
amount = int(input("Enter Amount: "))

try:
    balance = withdraw(balance, amount)
    print('Withdrawal successful')
    print('Remaining balance:', balance)
except InsufficientFundsError as e:
    print(e)