# Bank Account Challenge


import math

class InsufficientFundsError(Exception):
    pass

class IncorrectAmountError(Exception):
    pass


class BankAccount:
    acc_Counter = 100

    def __init__(self, name, balance):
        BankAccount.acc_Counter +=1
        self.__acc = BankAccount.acc_Counter  
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        if(amount > 0):
            self.__balance += amount


    def withdraw(self, amount):
        if (self.__balance >= amount):
            self.__balance -= amount
        else:
            raise InsufficientFundsError("Not Enough Funds!")
        
    def get_balance(self):
        return self.__balance
    
    def details(self):
        print  (f"Name: {self.name} AccountNo: {self.__acc} Balance: {self.__balance}")
    


account = BankAccount('James', 750.50)
MJ = BankAccount('Mary Jane', 950.75)
print(account.get_balance())

account.details()
MJ.details()

        