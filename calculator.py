print("enter first number:")
a=int(input())
print("enter second number:")
b=int(input())
print("choose 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
c=int(input())
match(c):
    case 1:
        print("the sum is",a+b)
        
    case 2:
        print("the difference is",a-b)
        
    case 3:
        print("the product is",a*b)
        
    case 4:
        if b!=0:
            print("the quotient is",a/b)
        else:
            print("division by zero is not allowed")
        
    case _:
        print("invalid choice")
print("calculator is done")        