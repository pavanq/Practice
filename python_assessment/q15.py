lst=[(1,2,3),(4,5),(1,2,3,8,0),(-1,-2)]
lst1=[]
lst2=[]
for i in lst:
    lst1.append(i)
    lst2.append(i[len(i)-1])
#print lst1
#print lst2
for i in range(len(lst2)):
    index=lst2.index(min(lst2))
    del lst2[index]
    print lst1[index]
    del lst1[index]
