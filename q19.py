string=raw_input("Enter a string: ")
d=dict((letter,string.count(letter)) for letter in set(string))
for k, v in d.iteritems():
    print '%s,%d' % (k, v)
