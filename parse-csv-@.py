import csv
names=[]

c=[]
i=0
with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    for list in csv_data:
         mystrings=''
         for x in list:
               
          mystrings+=x
         
         for c in mystrings:
            if c=='@':
             print(list) 
            
              
                
                            
                                  