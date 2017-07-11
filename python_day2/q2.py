print ("Enter temperature C/F")
x=raw_input()
if (x[-1]=="c" or "C"):
    print "fahrenheit is "+ str(float(x[:-1])*9/5 + 32)
elif (x[-1]=="f" or "F"):
    print "celsius is "+ str((float(x[:-1])-32)*5/9)
