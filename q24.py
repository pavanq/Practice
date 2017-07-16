line=raw_input("Enter text:")
lst=line.split(" ")
print [i for i in lst if i.isdigit()]
