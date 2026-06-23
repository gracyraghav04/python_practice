class Animal:
    @staticmethod
    def sound():
        print("Animal sound")


class Dog(Animal):
    @staticmethod
    def sound():
        print("Bark")


d = Dog()
d.sound()
#In Python, if you define a method inside a class using a normal def, it is treated as an instance method by default. The @staticmethod and @classmethod decorators explicitly indicate that the method should behave differently, i.e., no automatic self is passed (@staticmethod) or the class itself (cls) is passed instead of an instance (@classmethod).