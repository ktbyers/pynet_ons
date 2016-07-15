#!/usr/bin/env python

#### READ ####
f = open("my_file.txt")
for line in f:
    print line.strip()

f.seek(0)
my_content = f.readlines()
for line in my_content:
    print line.strip()

f.seek(0)
my_content = f.read()
for line in my_content.splitlines():
    print line

f.close()

# Most Pythonic way
with open("my_file.txt") as f:
    for line in f:
        print line.strip()


#### WRITE ####
f = open("new_file.txt", "w")
f.write('whatever2\n')
f.close()


#### APPEND ####
with open("new_file.txt", "a") as f:
    f.write('something else\n')
