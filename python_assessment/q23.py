filename="pavan.txt"
string=raw_input("Enter some text:")
with open(filename,'a') as file_object:
    file_object.write(string)
