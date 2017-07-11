x = [[0 for i in range(5)] for j in range(7)]
for i in range(1,8):
    for j in range(1,6):
       if (i==1 or i==4 or i==7) and (j==1 or j==2 or j==3 or j==4):
           x[i-1][j-1]=1
       elif (j==1):
            x[i-1][j-1]=1
       elif (j==5) and (i==1 or i==7):
            x[i-1][j-1]=1
for i in range(1,8):
    for j in range(1,6):
        if (x[i-1][j-1]==1):
            print ("* "),
        else:
            print ("  "),
    print '\n'
