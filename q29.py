lines = []
amount=0
while True:
    line = raw_input()
    if line:
        l=line.split()
        if (len(l)!=2):
            print ("Invalid Input")
            break
        if l[0]=='D':
            amount+=int(l[1])
        elif l[0]=='W':
            amount-=int(l[1])
        else :
            print ("Invalid Input")
            break
    else:
        break
print amount
