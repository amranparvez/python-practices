from pickle import TRUE


l={'alonso1':140 ,'alonso':55, 'modric':165}
c=list()
print(l)

print(sorted(l.items()))
for (i,j) in l.items():
    c.append((j,i))


print(c)
c=sorted(c)
c=sorted(c,reverse=True)
print(c)
#tups=l.items()
#print(tups)