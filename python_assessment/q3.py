def getkey(item):
    return item[-1]
lst=[(1,2,3),(4,5),(1,2,3,8,0),(-1,-2)]
x=sorted(lst,key=getkey)
print x
