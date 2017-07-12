"""week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
month=['january','february','march','april','may','june','july','august','september','october','november','december']
x=raw_input("Enter text:")
y=x
x=x.lower()
if (x in week or x in month):
    if (x in week):
        print y+" is",(week.index(x)+1),"day of the week"
    if (x in month):
        print y+" is",(month.index(x)+1),"month of the year"
else:
    print ("NO MATCH FOUND")"""


week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
month=['january','february','march','april','may','june','july','august','september','october','november','december']
weeknum=[1,2,3,4,5,6,7]
monthnum=[1,2,3,4,5,6,7,8,9,10,11,12]
dict1= {i:j for i,j in zip(week,weeknum)}
dict2={i:j for i,j in zip(month,monthnum)}
x=raw_input("Enter text:")
y=x
x=x.lower()
if (x in week or x in month):
    if (x in week):
        print y+" is",dict1[x],"day of the week"
    if (x in month):
        print y+" is",dict2[x],"month of the year"
else:
    print ("NO MATCH FOUND")
