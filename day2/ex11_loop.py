#!/usr/bin/env python

my_list = range(1, 50)

for i in my_list:
    if i == 13:
        continue
    print i
    if i == 39:
        break
