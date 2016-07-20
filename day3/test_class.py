#!/usr/bin/env python

class NetworkDevice(object):
    def __init__(self, ip_addr, username, password):
        self.ip = ip_addr
        self.username = username
        self.password = password

    def print_user(self):
        print "Hello world"
        self.x = 10
        print "Username is: {}".format(self.username)
        print "Password is: {}".format(self.password)


class ChildDevice(NetworkDevice):
    def __init__(self, ip_addr, username, password):
        print "Hello world"
        NetworkDevice.__init__(self, ip_addr, username, username)

    def print_user(self):
        print "Override method"


print
#rtr1 = NetworkDevice('10.10.10.10', 'admin', 'pass1')
#rtr1 = NetworkDevice()
#print rtr1.ip
#rtr1.print_user()

rtr2 = ChildDevice('10.10.10.10', 'admin', 'pass1')
print
print rtr2.ip
rtr2.print_user()
print
