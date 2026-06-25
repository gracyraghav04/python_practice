class Dog:
    def sound(self):
        print("bark");
class Human:
    def sound(self):
        print("hello");       #example of polymorphism as well.
h=Human();
h.sound();   
def talk(obj):   #duck typing 
    obj.sound();#python does not see the type if object;it only sees behaviour of object.
talk(Dog());
talk(Human());                    
