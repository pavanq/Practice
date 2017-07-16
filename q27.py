t1=(1,2,3,4,5,6,7,8,9,10)
t2=()
for i in range(len(t1)):
    if t1[i]%2!=0:
        t2=t2 + (t1[i],)
print t2
        
