class Student:
    def __init__(self):
        print("object created")
        self.name="Elly"
        self.age=20
       
    def __init__(self,n,a): # overwrite first constructor
        self.name=n
        self.age=a
s2=Student("John",22)
print(s2.name)
print(s2.age)
  
s1=Student("Alice",21)  
print(s1.name)
print(s1.age)
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)
a1 = BankAccount("Elly", 5000)
a2 = BankAccount("Rahul", 12000)

a1.show_balance()
a2.show_balance()