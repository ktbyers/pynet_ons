#!/usr/bin/env python

with open("show_version.txt") as f:
    show_ver = f.read().splitlines()

for line in show_ver:
    if 'Processor board ID' in line:
        _, serial_number = line.split("Processor board ID")

print "\nSerial Number is {}\n".format(serial_number) 
