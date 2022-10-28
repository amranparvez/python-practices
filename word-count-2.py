f_handle=open('diction.txt')
counts=dict()
for line in f_handle:
      words=line.split()    
      print(words)
      for word in words:
          counts[word]=counts.get(word,0)+1

lst=list()
for k,v in counts.items():
    #print(k,v)
    
    newtuple=(v,k)
    lst.append(newtuple)

print(lst)
lst=sorted(lst,reverse=True)
for v,k in lst[:20]:
    print(k,v)