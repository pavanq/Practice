class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
class male(person):
    gender="Male"
    def __init__(self,firstname,lastname):
        person.__init__(self,firstname,lastname)
class female(person):
    gender="Female"
    def __init__(self,firstname,lastname):
        person.__init__(self,firstname,lastname)
person1=male("sujith","kumar")
person2=female("Aruna","kumari")

print(person1.gender)
print (person2.gender)  
