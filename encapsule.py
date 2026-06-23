class student:
    def __init__(self,n,a):
        self.name=n #public attribute #convention plus fully accessile

        self._age=a #protected attribute # convention plus fully accessile
        self.__grade="A" #private attribute #raise error if tried to  get accessed
s1=student("Elly",20)  
s1.name="akku"
    
print(s1.name)
print(s1._age)

print(s1.__grade)
