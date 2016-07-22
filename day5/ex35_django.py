#!/usr/bin/env python
"""
Exercise 35
Write a Python script that retrieves all of the network devices from the database
Using this data, make a Netmiko connection to each device.
Retrieve 'show arp'.
Record the time that the program takes to execute.
"""
from datetime import datetime

import django
from netmiko import ConnectHandler
from net_system.models import NetworkDevice


def create_netmiko_dict(net_device):
    """
    From a Django NetworkDevice create a dict for netmiko.
    """
    my_device = {}
    my_device['device_type'] = net_device.device_type
    my_device['ip'] = net_device.ip_address
    my_device['username'] = net_device.credentials.username
    my_device['password'] = net_device.credentials.password
    return my_device

def main():
    """
    Write a Python script that retrieves all of the network devices from the database
    Using this data, make a Netmiko connection to each device.
    Retrieve 'show arp'.
    Record the time that the program takes to execute.
    """
    start_time = datetime.now()
    django.setup()
    my_devices = NetworkDevice.objects.all()
    print
    for a_device in my_devices:
        a_device_netmiko = create_netmiko_dict(a_device)
        remote_conn = ConnectHandler(**a_device_netmiko)
        show_arp = remote_conn.send_command_expect("show arp")
        print a_device.device_name
        print '-' * 80
        print show_arp
        print '-' * 80
        print
    print ">>>>>>>> Total Time: {}".format(datetime.now() - start_time)
    print

if __name__ == "__main__":
    main()
