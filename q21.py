lst=[12,24,35,24,88,120,155,88,120,155]
s=[]
for i in lst:
    if i not in s:
        s.append(i)
print s
