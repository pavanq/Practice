from __future__ import print_function
n=input("Enter a positive integer:")
while (n!=1):
    print (n,sep=',',end=',')
    if (n%2==0):
        n=n/2
    else:
        n= 3*n+1   
print (1)
