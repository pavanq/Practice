a=input("Enter a:")
b=input("Enter b:")
x=input("0.NONE\n1.ADDITION a+b\n2.SUBTRACTION a-b\n3.MULTIPLICATION a*b\n4.DIVISION a/b\n")
class values:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Initialization of class VALUES")
        print "The result is",
    def addition(self):
        print a+b
    def subtract(self):
        print a-b
    def multiply(self):
        print a*b
    def division(self):
        print float(a)/b
pair=values(a,b)
if x==1:
    pair.addition()
elif x==2:
    pair.subtract()
elif x==3:
    pair.multiply()
elif x==4:
    pair.division()
else:
    print("DONE!")
