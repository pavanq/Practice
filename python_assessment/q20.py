s=raw_input("Enter a string: ")
string=s.split(" ")
d=dict((letter,string.count(letter)) for letter in set(string))
for k in sorted(d):
    print '%s:%d' % (k, d[k])
