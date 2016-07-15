#!/usr/bin/env python

my_list = range(5)
my_list.append('whatever')
my_list.append(-19)
print my_list.pop(0)

print "Length of list: {}".format(len(my_list))
my_list.sort()
print my_list
