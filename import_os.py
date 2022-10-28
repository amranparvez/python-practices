
import os
from datetime import datetime
from stat import ST_MTIME


#print(dir(os))

#print(os.getcwd())
os.chdir('/Users/palas/OneDrive/Desktop/newdir')
#print(os.getcwd())

#os.mkdir("test-5")
#os.makedirs("test-4/test-3")
print(os.getcwd())
print(os.listdir())
#os.rmdir('test-4')
#os.rmdir('test-5')
#os.rmdir('test-2')
print(os.listdir())
#os.removedirs('test-5')
#os.rename('test-4','test-420')
#print(os.listdir())
file_stat=os.stat('test-5').st_mtime
print(file_stat)

print(datetime.fromtimestamp(file_stat))

for dir_path,dir_name,file_name in os.walk(os.getcwd()) :
     print('current path ',dir_path )
     print('current folder ',dir_name )
     print('current file name ',file_name )
     
print(os.environ.get('C:/Users/palas/OneDrive/Desktop/data analyst/python') )    