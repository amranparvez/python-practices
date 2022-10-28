
with open('test-2.txt','w') as f:
 f.write('A quick brown fox jumps right over the dog')
with open('test-2.txt','r') as rf:
 with open('test-3.txt','w') as wf:
     for line in rf: 
      wf.write(line)
