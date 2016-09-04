#!/usr/bin/python

macaddr = "A5:BA:DB:20:93:0a"
prefix_mac = macaddr[:-3]
print prefix_mac
last_two = macaddr[-2:]
print last_two
plus_one = int(last_two, 16) + 1
print plus_one
if plus_one in range(10):
    new_last_two = hex(plus_one)[2:]
    print new_last_two
    new_last_two = '0' + new_last_two
else:
    new_last_two = hex(plus_one)[2:]
    print new_last_two
    if len(new_last_two) == 1:
        new_last_two = '0' + new_last_two
        print new_last_two
new_mac = prefix_mac  + ':' +  new_last_two
print new_mac.upper()

