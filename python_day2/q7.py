x = [[0 for i in range(5)] for j in range(7)]
for i in range(1,8):
    for j in range(1,6):
       if (j==1 or j==5) and (i==2 or i==3 or i==4 or i==5 or i==6):
           x[i-1][j-1]=1
       elif (i==1 or i==7) and (j!=5):
            x[i-1][j-1]=1
for i in range(1,8):
    for j in range(1,6):
        if (x[i-1][j-1]==1):
            print ("* "),
        else:
            print ("  "),
    print '\n'
