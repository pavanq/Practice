class Error(Exception):
   """Base class for other exceptions"""
   pass

class LengthTooSmallError(Error):
   """Raised when the input Length is too small"""
   pass

class LengthTooLargeError(Error):
   """Raised when the input Length is too large"""
   pass

number = 10

while True:
   try:
       i = len(raw_input("Enter some text: "))
       if i < number:
           raise LengthTooSmallError
       elif i > number:
           raise LengthTooLargeError
       break
   except LengthTooSmallError:
       print("This Length is too small, try again!")
   except LengthTooLargeError:
       print("This Length is too large, try again!")

print("Congratulations! You guessed length correctly.")
