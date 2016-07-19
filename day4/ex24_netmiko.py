#!/usr/bin/env python
"""Exercises using Netmiko"""
from getpass import getpass
from netmiko import ConnectHandler

def save_file(filename, show_run):
    """Save the show run to a file"""
    with open(filename, "w") as f:
        f.write(show_run)

def main():
    """Exercises using Netmiko"""
    rtr1_pass = getpass("Enter router password: ")
    sw1_pass = getpass("Enter switch password: ")
    pynet_rtr1 = {
        'device_type': 'cisco_ios',
        'ip':   '184.105.247.70',
        'username': 'pyclass',
        'password': rtr1_pass,
    }

    pynet_sw1 = {
        'device_type': 'arista_eos',
        'ip':   '184.105.247.72',
        'username': 'admin1',
        'password': sw1_pass,
    }

    for a_device in (pynet_rtr1, pynet_sw1):
        net_connect = ConnectHandler(**a_device)
        print "Current Prompt: " + net_connect.find_prompt()

        show_arp = net_connect.send_command("show arp")
        print
        print '#' * 80
        print show_arp
        print '#' * 80
        print

        show_run = net_connect.send_command("show run")
        filename = net_connect.base_prompt + ".txt"
        print "Save show run output: {}\n".format(filename)
        save_file(filename, show_run)

if __name__ == "__main__":
    main()

