# Practice Question 1 :
# Que : - Create Account class with 2 attributes - balance and account no. 
#         create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print("Total balance : ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print("Total balance : ", self.get_balance())


    def get_balance(self):
         return self.balance

acc1 = Account(10000, 12345)
print("Balance : ", acc1.balance)
print("Account Number : ", acc1.acc_no)

acc1.debit(1000)
acc1.credit(500)
acc1.debit(4900)
acc1.credit(7600)
print(acc1.get_balance())