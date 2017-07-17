x=input("Enter a positive integer:")
while (x>2):
    if x%2==0:
        x=x/2
    else:
        print("NOT A POWER OF 2")
        break
if (x==2):
    print ("POWER OF 2")
