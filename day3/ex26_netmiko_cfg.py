#!/usr/bin/env python
"""Exercises using Netmiko"""
from getpass import getpass
from netmiko import ConnectHandler

def main():
    """Exercises using Netmiko"""
    sw1_pass = getpass("Enter switch password: ")

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': sw1_pass,
    }

    cfg_commands = [
        'vlan 901',
        'name red',
    ]

    net_connect = ConnectHandler(**pynet_sw1)
    print "Current Prompt: " + net_connect.find_prompt()

    print "\nConfiguring VLAN"
    print "#" * 80
    output = net_connect.send_config_set(cfg_commands)
    print output
    print "#" * 80
    print

    print "\nConfiguring VLAN from file"
    print "#" * 80
    output = net_connect.send_config_from_file("vlan_cfg.txt")
    print output
    print "#" * 80
    print


if __name__ == "__main__":
    main()


#output = net_connect1.send_config_set(cfg_commands)
#print output

#print output
