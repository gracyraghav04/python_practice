class student:
    def __init__(self,n):
        self.name=n #public attribute #convention plus fully accessile

        self._age=20 #private attribute # convention plus fully accessile
        self._grade="A" #protected attribute #raise error if tried to  get accessed
s1=student("Elly")  
s1._age=21      
print(s1.name)
print(s1._age)
print(s1._grade)
