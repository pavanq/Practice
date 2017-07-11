m=input()
n=input()
x = [[0 for i in range(n)] for j in range(m)]
for i in range(1,m+1):
    for j in range(1,n+1):
       if (i==1 or i==m) and (j!=1 and j!=n):
           x[i-1][j-1]=1
       elif (j==1) and (i!=1 and i!=m):
            x[i-1][j-1]=1
       elif (j!=2) and (i==m/2+1):
            x[i-1][j-1]=1
       elif (j==n) and (i==2 or i>=m/2+1) and (i!=m):
            x[i-1][j-1]=1
for i in range(1,m+1):
    for j in range(1,n+1):
        if (x[i-1][j-1]==1):
            print ("* "),
        else:
            print ("  "),
    print '\n'
