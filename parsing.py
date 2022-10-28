import os 
for f in os.listdir():
    f_name,f_ext=os.path.splitext(f)
    if(f_ext=='.pdf'):
     print(f_name, '',f_ext)

# no need to re arrange#
#strip() 