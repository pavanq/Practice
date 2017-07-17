line=raw_input("Enter text:")
lst=line.split("@")
company=lst[1].split(".")
print company[0]
