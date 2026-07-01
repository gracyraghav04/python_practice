try:
    num = int(input())

    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter numbers only")
finally:
    print("program ends")    #will always execute whether there is exception or not