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

class Employee:
    company = "Google"#class variable

    def __init__(self, name):
        self.name = name #instance variable

e1 = Employee("Elly")
e2 = Employee("Rahul")

print(e1.company)
print(e2.company)
print(e1.name)
print(e2.name)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self): #instance method; works with  the object's data.
        print("Balance:", self.balance)

a1 = BankAccount(5000)
a1.show_balance()