line=raw_input("Enter text : ")
digitcount,lettercount=0,0
for i in line:
    if i.isdigit():
        digitcount+=1
    if i.isalpha():
        lettercount+=1
print ("LETTERS "+str(lettercount))
print ("DIGITS "+str(digitcount))
