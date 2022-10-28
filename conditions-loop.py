from tkinter.font import BOLD
from tkinter.tix import Tree



num=569;
J=False


for i in range(2,num):

   if(num%i):
        j=False
        break
   else :
              i=i+1; 
              j=True
     

if j==False :
         print("not prime is ",num)
else:  print("prime is ",num)
