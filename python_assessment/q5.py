line=raw_input("Enter list of values separated by comma :")
lst=line.split(",")
for i in range(len(lst)):
    lst[i]=int(lst[i])
lst2=[]

for i in range(len(lst)):
        lst2.append(min(lst))
        del lst[lst.index(min(lst))]
        if (min(lst)!=lst2[-1]+1):
            print lst2[-1]+1
            break
