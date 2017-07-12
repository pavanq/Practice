import sys
a=raw_input('Enter the string:')
for i in range(len(a)):
    if a[i]!=a[len(a)-i-1]:
        print "not palindrome"
        sys.exit()
print "palindrome"
