import re

#x=str()
x='my 7 likebale num435345ber are2 ,3,5,,131,3791,123,4343,6565,678567567'

y=re.findall('[0-9]+',x)
print(y)    