#!/usr/bin/env python

class net_device(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def test_method(self):
        print "Device IP is: {}".format(self.ip_addr)
        print "Username is: {}".format(self.username)


if __name__ == "__main__":
    rtr1 = net_device('10.22.1.1', 'admin', 'passw')

    print rtr1.ip_addr
    print rtr1.username

    rtr1.test_method()
