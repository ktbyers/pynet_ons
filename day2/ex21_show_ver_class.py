#!/usr/bin/env python
"""
Use regular expressions to obtain serial number, vendor, model, os_version, and uptime from show
version output.
"""
import re


def read_file(filename):
    """Read filename; return contents as one string."""
    with open(filename) as my_file:
        return my_file.read()


class NetDeviceInventory(object):
    """Parse show version, retain attributes"""
    def __init__(self, show_ver):
        self.show_ver = show_ver
        self.serial_number = ''
        self.vendor = ''
        self.model = ''
        self.os_version = ''
        self.uptime = ''

    def find_serial_number(self):
        """
        Find the serial number in show version output.

        Example: Processor board ID FTX1512038X
        """
        match = re.search(r"Processor board ID (.*)", self.show_ver)
        if match:
            self.serial_number = match.group(1)

    def find_vendor(self):
        """
        Example:
        Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE...
        """
        match = re.search(r"Cisco IOS Software", self.show_ver)
        if match:
            self.vendor = 'Cisco'

    def find_model(self):
        """
        Example:
        Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
        """
        match = re.search(r"^Cisco (.*?) .* bytes of memory.$", self.show_ver, flags=re.M)
        if match:
            self.model = match.group(1)

    def find_os_version(self):
        """
        Example:
        Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE...
        """
        match = re.search(r"Cisco IOS Software.* Version (.*), .*", self.show_ver)
        if match:
            self.os_version = match.group(1)

    def find_uptime(self):
        """
        Example:
        pynet-rtr1 uptime is 3 weeks, 1 day, 3 hours, 52 minutes
        """
        match = re.search(r".* uptime is (.*)", self.show_ver)
        if match:
            self.uptime = match.group(1)

def main():
    """
    Use regular expressions to obtain serial number, vendor, model, os_version, and uptime from
    show version output.
    """
    my_file = "show_version.txt"

    show_ver = read_file(my_file)
    net_dev_obj = NetDeviceInventory(show_ver)
    net_dev_obj.find_serial_number()
    net_dev_obj.find_vendor()
    net_dev_obj.find_model()
    net_dev_obj.find_os_version()
    net_dev_obj.find_uptime()

    print
    print "Vendor: {}".format(net_dev_obj.vendor)
    print "Model: {}".format(net_dev_obj.model)
    print "OS Version: {}".format(net_dev_obj.os_version)
    print "Serial Number: {}".format(net_dev_obj.serial_number)
    print "Uptime: {}".format(net_dev_obj.uptime)
    print

if __name__ == "__main__":
    main()
