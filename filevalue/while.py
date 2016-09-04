#!/usr/bin/python
x = ''
while x != 'q' :
    print 'hello'
    x = raw_input("Please input something,q for quit")
    if not x :
        break 
    if x == 'quit':
        continue
    print 'continue'
else:
    print 'world'
