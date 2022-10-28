import csv


with open ('biostats.csv','r') as csv_file:

 csv_reader=csv.reader(csv_file)
 with open('biostats1.csv','w') as csv_file1:
     csv_writer=csv.writer(csv_file1,delimiter='\t')
     for line in csv_reader:
        csv_writer.writerow(line)
with open ('biostats1.csv','r') as csv_file1: 
 for line1 in csv_file1:
      print(line1)       