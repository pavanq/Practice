text=raw_input("Enter additive sequence:")
line=text.split(',')
lst=[]
print line
for i in line:
    i=int(i)
    lst.append(i)
print  lst
i=0
j=1
k=2
while (lst[k]==lst[i]+lst[j]): 
    i+=1
    j+=1
    if (k>=len(lst)-1):
        print ("Additive sequence")
        break
    k+=1
if (k<len(lst)-1):
        print ("Not an Additive sequence")
