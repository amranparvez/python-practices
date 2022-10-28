
from unicodedata import name


client_information={'name':'albion' ,"age":45, "martial_status":"married", 'vehicles':['CAR',"zeep","private plane"]}

print(client_information);
print(client_information['martial_status']);

client_information['phone']="+440276890";
print(client_information.get('phone'));

print(client_information.get('sex','no entry'));
print(client_information);
print(client_information['martial_status']);


age=client_information.pop('age')
print(client_information.get('age'));
print(age);

for key,value in client_information.items():
    print(key,value);