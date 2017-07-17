class Error(Exception):
   """Base class for other exceptions"""
   

class valuetoosmall(Error):
   """Raised when the input Length is too small"""
   

class valuetoolarge(Error):
   """Raised when the input Length is too large"""
   

while True:
    try:
        n=input("Enter a number:")
        if (n<10):
            raise valuetoosmall
        if (n>10):
            raise valuetoolarge
        else :
            print("perfect")
            break
    except valuetoosmall:
        print ("value is too small")
    except valuetoolarge:
        print ("value is too large")
