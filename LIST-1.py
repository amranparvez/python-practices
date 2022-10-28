


from audioop import reverse
from pickle import TRUE


DEVICES=("BACBON","HP SPECTRE X360","HP ENVY X360","MICROSOFT SURFACE BOOK 2")
extended_devices=("wacom h27 ","benq interactive flat ")
device_1=["d","c" ,"a","b" ]
devices_2=["ipad10"]
""" print(DEVICES[-1])
print(DEVICES[0:2])
print(DEVICES[:2])
print(DEVICES[-1:0])


DEVICES.extend(extended_devices)
print(DEVICES);

DEVICES.insert(0,extended_devices)
print(DEVICES)

extended_devices.append(DEVICES)
print(extended_devices)

device_1.sort(reverse=True);
print(device_1);
sorted_device=sorted(device_1)
print(device_1)

print(device_1.index('a'))
"""
# mutuable  tuple are in first brackets ()
DEVICES=extended_devices
print(DEVICES)
print(extended_devices)
DEVICES.insert(0,"ipad10")
print(DEVICES)

#immutable not immutable in tuple



# sets are in 2nd brackets {}

