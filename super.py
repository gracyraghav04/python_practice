class Animal:
    def __init__(self):
        print("Animal Constructor")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")


d = Dog()
#Inheritance automatically gives access to parent members. super() is used when the child class wants to explicitly invoke the parent class's implementation (especially constructors and overridden methods) instead of replacing it completely.