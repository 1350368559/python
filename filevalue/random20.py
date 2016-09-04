#!/usr/bin/python

import random
import sys

print 'The random have been created'
random_num = random.randint(1,20)

for i in xrange(1,7) :
    enter_num = int(raw_input('Please input guess num'))
    if random_num < enter_num:
        print 'biger'
    elif random_num > enter_num:
        print 'lower'
    elif random_num == enter_num:
        print 'you are win'
        sys.exit()
print 'game over'
