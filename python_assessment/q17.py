from math import pi
class circle:   
    def __init__(self,r):
        self.radius=r
        print ("Initializing class CIRCLE")
    def getarea(self):
        area= pi*r*r
        print ("Computing area by class method")
        print("The area is "+str(area))
r=input("Enter radius:")
c1=circle(r)
c1.getarea()
