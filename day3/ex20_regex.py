#!/usr/bin/env python
"""
Use regular expressions to obtain serial number, vendor, model, os_version, and uptime from show
version output.
"""
import re
from pprint import pprint


def read_file(filename):
    """Read filename; return contents as one string."""
    with open(filename) as my_file:
        return my_file.read()

def find_serial_number(show_ver):
    """
    Find the serial number in show version output.

    Example: Processor board ID FTX1512038X
    """
    match = re.search(r"Processor board ID (.*)", show_ver)
    if match:
        return match.group(1)
    return ''

def find_vendor(show_ver):
    """
    Example:
    Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE...
    """
    match = re.search(r"Cisco IOS Software", show_ver)
    if match:
        return 'Cisco'
    return ''

def find_model(show_ver):
    """
    Example:
    Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
    """
    match = re.search(r"^Cisco (.*?) .* bytes of memory.$", show_ver, flags=re.M)
    if match:
        return match.group(1)
    return ''

def find_os_version(show_ver):
    """
    Example:
    Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE...
    """
    match = re.search(r"Cisco IOS Software.* Version (.*), .*", show_ver)
    if match:
        return match.group(1)
    return ''

def find_uptime(show_ver):
    """
    Example:
    pynet-rtr1 uptime is 3 weeks, 1 day, 3 hours, 52 minutes
    """
    match = re.search(r".* uptime is (.*)", show_ver)
    if match:
        return match.group(1)
    return ''

def main():
    """
    Use regular expressions to obtain serial number, vendor, model, os_version, and uptime from
    show version output.
    """
    my_file = "show_version.txt"

    my_device = {}

    show_ver = read_file(my_file)
    my_device['serial_number'] = find_serial_number(show_ver)
    my_device['vendor'] = find_vendor(show_ver)
    my_device['model'] = find_model(show_ver)
    my_device['os_version'] = find_os_version(show_ver)
    my_device['uptime'] = find_uptime(show_ver)

    print
    pprint(my_device)
    print

if __name__ == "__main__":
    main()
