file_object=open('test.txt','r')
#print(file_object.name)
print(file_object.mode)
for line in file_object:
 print(line, end='')

file_object.close()
# with open () as file_object