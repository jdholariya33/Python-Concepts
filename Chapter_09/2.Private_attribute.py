# Privte(like) Attributes and Methods : -
# Conceptual Implementations in python :
# Private Attributes and Methods are meant to be used only within the class and are not accessible from outside the class.

# Syntax : __attribute_name

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")

print("Account Number : ", acc1.acc_no)
# print(acc1.__acc_pass)    -->     Error : 'Account' object has no attribute '__acc_pass'
print("Password : ",acc1.reset_pass())  # Return None