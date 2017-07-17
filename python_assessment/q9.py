from __future__ import print_function
def validate(s):
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
    if (len(s)>=6 and len(s)<=16 and number(s) and upper(s) and lower(s) and char(s)):
        print ("valid")
    else:
        print ("Not valid")
if __name__ == "__main__":
    line=raw_input("Enter password:")
    c=["$","#","@"]
    validate(line)
