
import os
from datetime import datetime

os.chdir('/Users/palas/OneDrive/Desktop/newdir')
#print(os.environ.get('HOME'))
#file_path=os.environ.get('_/Users/palas/OneDrive/Desktop/newdir_')+'test.txt'
file_path=os.path.join('/Users/palas/OneDrive/Desktop/newdir/')+'test.txt'
print(file_path)
print(os.path.basename('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print( dir(os.path))