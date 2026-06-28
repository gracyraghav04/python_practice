from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


# Child Class 1
class UPI(Payment):

    def pay(self):
        print("Payment done using UPI")


# Child Class 2
class CreditCard(Payment):

    def pay(self):
        print("Payment done using Credit Card")


# Creating objects
u = UPI()
c = CreditCard()

u.pay()
c.pay()