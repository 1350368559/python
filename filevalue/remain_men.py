#!/usr/bin/python

with open('/proc/meminfo') as fd1:
    for line1 in fd1:
        if line1.startswith('MemTotal'):
            memtotal = line1.split()[1]
            continue
        if line1.startswith('MemFree'):
            memfree = line1.split()[1]
            break
print "%.2f,%s,%.2f,%s" (int(memtotal)/1024.0) +'M', (int(memfree)/1024.0) +'M'
