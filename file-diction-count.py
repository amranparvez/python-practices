f_handle=open('diction.txt')
counts=dict()
for line in f_handle:
      words=line.split()    
      print(words)
      for word in words:
          counts[word]=counts.get(word,0)+1


bigword=None
bigcount=None

for word ,count in counts.items():
      if bigcount is None or count>bigcount:
         bigcount=count
         bigword =word 
print( bigword,bigcount)      