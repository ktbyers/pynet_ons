#!/usr/bin/env python
'''
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
'''
from getpass import getpass
from snmp_helper import snmp_get_oid_v3, snmp_extract

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'

def main():
    '''
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
    prints out both the MIB2 sysName and sysDescr.
    '''
    my_key = getpass(prompt="Auth + Encryption Key: ")

    # SNMPv3 Connection Parameters
    ip_addr = '184.105.247.70'
    a_user = 'pysnmp'
    auth_key = my_key
    encrypt_key = my_key
    snmp_user = (a_user, auth_key, encrypt_key)
    pynet_rtr1 = (ip_addr, 161)

    for a_device in (pynet_rtr1,):
        print "\n*********************"
        for the_oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_get_oid_v3(a_device, snmp_user, oid=the_oid)
            output = snmp_extract(snmp_data)
            print output
        print "*********************"
    print

if __name__ == "__main__":
    main()
