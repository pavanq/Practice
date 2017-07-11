s=raw_input()
c=["$","#","@"]
def number(s):
    return any(i.isdigit() for i in s)
def upper(s):
    return any(i.isupper() for i in s)
def lower(s):
    return any(i.islower() for i in s)
def char(s):
    for i in s:
        if (i in c):
            return True
while (len(s)<6 or len(s)>16 or not number(s) or not upper(s) or not lower(s) or not char(s)):
    print ("Minimum length is 6")
    print ("Maximum length is 16")
    print ("At least 1 number between [0-9]")
    print ("At least 1 letter between [A-Z]")
    print ("At least 1 letter between [a-z]")
    print ("At least 1 character from [$#@]")
    s=raw_input()


    
