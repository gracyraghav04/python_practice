class Student:
    def __init__(self, n):
        self.name = n
    def __str__(self):#human readable output
        return(f"student name:{self.name}")

s1=Student("Elly")
print(s1)    
class Student:
    def __init__(self, n):
        self.name = n
    def __repr__(self):#developer debugging representation
        return(f"Student('{self.name}')")

s1=Student("Elly")
print(s1)    

