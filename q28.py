from __future__ import print_function
line=raw_input().split(",")
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
for s in line:
    if (len(s)>=6 and len(s)<=16 and number(s) and upper(s) and lower(s) and char(s)):
        print (s,sep=",")
