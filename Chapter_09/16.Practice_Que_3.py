# Practice Question 3 :
# Que : - Create a class called Order which stores item and its price.
#         Use Dunder function __gt__() to convey that:
#         order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        if self.price > ord2.price:
            print(f"{self.item} price is greater than {ord2.item} price")
        else:
            print(f"{ord2.item} order2 price is greater than {self.item} price")

ord1 = Order("Bat", 14000)
ord2 = Order("Ball", 3000)

res = ord1 > ord2
print(res)
