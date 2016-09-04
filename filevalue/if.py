#!/usr/bin/python

score = int(raw_input("please input a num"))
print(type(score))
if score >= 90:
    print 'A'
    print 'very good'
elif score >= 80:
    print 'B'
    print 'good'
elif score >= 70:
    print 'C'
else:
    print 'D'
print 'end'
