#!/usr/bin/python

with open('/tmp/tmp.txt') as fd:
    while True:
        line = fd.readline()
        if not line:
            break
        print line
