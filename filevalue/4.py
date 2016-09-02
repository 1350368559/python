#!/usr/bin/python
info = {}
name = raw_input("Please input name:")
age = raw_input("Please input age:")
gender = raw_input('Please input (M/F)')

info['name'] = name
info['age'] = age
info['gender'] = gender
for k,v in info.items():
    print "%s: %s" % (k, v)
print 'main end'
