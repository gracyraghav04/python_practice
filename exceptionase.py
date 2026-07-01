try:
    print(10 / 0)

except Exception as e:
    print(e)
     # e has actual error object which can be used to get the error msg
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")    #when pyhton needs to throw an explicit error 
    '''most common exceptions
    zeroDivisionError
    ValueError
    TypeError
    IndexError
    KeyError
    FileNOtFoundError
    '''