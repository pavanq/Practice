h=input("No. of heads:")
l=input("No. of legs:")
r=(l-2*h)/2
c=h-r
if ((l-2*h)%2==0 and r>=0 and c>=0):
        print "No. of rabbits : ",r,"\nNo. of chickens : ",c
    else :
        print "Invalid Input"
