m=input("Enter number of rows: ")
n=input("Enter number of columns: ")
x = [[0 for i in range(n)] for j in range(m)]
for i in range(1,m+1):
    for j in range(1,n+1):
       if (j==1 or j==n):
           x[i-1][j-1]=1
i=2
j=2
if (m%2==0):
    k=m/2
else:
    k=(m+1)/2
if (n%2==0):
    l=n/2
else:
    l=(n+1)/2
while(i<=k and j<=l):
    x[i-1][j-1]=1
    i=i+1
    j=j+1
i=2
j=n-1
while (i<=k and j>l):
    x[i-1][j-1]=1
    i=i+1
    j=j-1
if (m%2==0):
    k=m/2
else:
    k=(m+1)/2
if (n%2==0):
    l=n/2
else:
    l=(n+1)/2
if (m<n):
    i=k+1
    j=k+1
    f=n-k
    while (j<=f):
        x[i-1][j-1]=1
        x[i-1][f-1]=1
        i=i+1
        j=j+1
        f=f-1  
for i in range(1,m+1):
    for j in range(1,n+1):
        if (x[i-1][j-1]==1):
            print ("* "),
        else:
            print ("  "),
    print '\n'
