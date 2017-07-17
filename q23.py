#n=input("No. of values:")
#lst=[]
#for i in range(0,n):
    #print i
    #lst[i]=input("Enter value:")
#print lst
lst=[1,2,3,4,5,6,7,8,9,10]
value=input("Enter value to be searched:")
def binary(data,key,start,end):
    mid=(start+end)/2
    if data[mid]==key:
        return mid
    if data[mid]>key:
        return binary(data,key,start,mid)
    else:
        return binary(data,key,mid+1,end)
if (lst[len(lst)-1]<value or lst[0]>value):
    print ("Value not found")
else :
    index=binary(lst,value,0,len(lst)-1)
    print index
