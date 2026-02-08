l=[]
for i in range(5):
    n=int(input())
    l.append(n)
print(f"maximum number is {max(l)}") #max element using built in function
print("the list is",l)
min_num=l[0]
for element in l:
    if(element<min_num):
        min_num=element
print(f"minimum element is {min_num}")   
print("minimum element is",min_num)   