#!/usr/bin/python

import time
for i in xrange(10):
    if i == 3:
        continue 
    elif i == 5:
        break    
    elif i == 6:
        pass  
    time.sleep(1)
    print i
else:
    print "main end"

