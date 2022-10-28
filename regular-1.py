
import re

f_handle=open('diction1.txt')
for line in f_handle:
      words=line.split() 
      for x in words:
        y=re.findall('^[0-9]+',x)
        print(y)