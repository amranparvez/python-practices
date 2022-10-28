f_handle=open('diction.txt')
counts=dict()
for line in f_handle:
      words=line.split()    
      print(words)
      for word in words:
          counts[word]=counts.get(word,0)+1


#print(counts)
lst=list()
for key,val in counts.items():
    newtuple=(val,key)
    lst.append(newtuple)

lst=sorted(lst,reverse=True)
for val,key in lst[:10]:
    print(key,val)  

