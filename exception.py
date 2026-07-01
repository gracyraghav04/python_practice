# Arun-time error that interferes with the normal operation of the program is exception.
try:
    num = int(input("Enter Number: ")) #exception handling
    print(10 / num)

except:
    print("Error") 

#specific exception handling best practice
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")    
    