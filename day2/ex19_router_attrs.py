#!/usr/bin/env python

def read_file(filename):
    with open(filename) as f:
        return f.read()

def find_serial_number(show_ver):
    serial_number = ''
    for line in show_ver.splitlines():
        if 'Processor board ID' in line:
            _, serial_number = line.split("Processor board ID")
    return serial_number

def find_vendor(show_ver):
    pass

def find_model(show_ver):
    pass

def find_os_version(show_ver):
    pass

def find_uptime(show_ver):
    pass


my_file = "show_version.txt"
show_ver = read_file(my_file)
serial_number = find_serial_number(show_ver)
print "\nSerial Number is {}\n".format(serial_number) 
