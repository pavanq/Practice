x=input("0.DONE!!! \n1.ADD a+b \n2.SUBTRACT a-b \n3.MULTIPLY a*b \n4.DIVISION a/b \n ")
while (x!=0):
    if (x in [1,2,3,4]):
        a=float(input("Enter a:"))
        b=float(input("Enter b:"))
    if (x==1):
        print a+b
    elif (x==2):
        print a-b
    elif (x==3):
        print a*b
    elif (x==4):
        print a/b
    else:
        print ("Enter valid input")
   x=input("0.DONE!!! \n1.ADD a+b \n2.SUBTRACT a-b \n3.MULTIPLY a*b \n4.DIVISION a/b \n ")
