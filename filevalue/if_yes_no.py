#!/usr/bin/python

yn = raw_input("Please input [Yes/No]:")
yn = yn.lower()
if yn == 'y' or yn == 'yes':
    print "program is running"
elif yn == 'n' or yn == 'no':
    print 'program is exit'
else:
    print "please input [yes|no]"

