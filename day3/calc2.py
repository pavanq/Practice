x=raw_input("0.DONE!!! \n1.ADD a+b \n2.SUBTRACT a-b \n3.MULTIPLY a*b \n4.DIVISION a/b \n ")
if (x not in ['1','2','3','4','0']):
    print ("Enter valid input")
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
while (x!=0):
    if (x in [1,2,3,4]):
        a=raw_input("Enter a:")
        b=float(input("Enter b:"))
    if (x==1):
        print add(a,b)
    elif (x==2):
        print subtract(a,b)
    elif (x==3):
        print multiply(a,b)
    elif (x==4):
        print division(a,b)
    x=input("0.DONE!!! \n1.ADD a+b \n2.SUBTRACT a-b \n3.MULTIPLY a*b \n4.DIVISION a/b \n ")
