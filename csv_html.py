import csv

html_output=''
names=[]

with open('patrons.csv','r') as data_file:
    csv_data=csv.reader(data_file)
    #print(list(csv_data))
    next(csv_data)
    next(csv_data)
    for line in csv_data:
      names.append(f"{line[0]} {line[1]}")
      #print(line)
    
