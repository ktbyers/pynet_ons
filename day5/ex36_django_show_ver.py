#!/usr/bin/env python
"""
Exercise 36
Integrate your show version functions into the system (for the two Cisco devices).
In other words, use the database information to make a Netmiko connection.
From these Netmiko connections retrieve show version and save the vendor, model,
os_version, serial_number and uptime_seconds to the database.
"""
import re

import django

from netmiko import ConnectHandler
from net_system.models import NetworkDevice
from show_version import NetDeviceInventory
from ex35_django import create_netmiko_dict

def convert_uptime_to_seconds(uptime):
    """
    Convert Cisco router uptime string to seconds
    4 weeks, 2 days, 1 hour, 39 minutes
    2 weeks, 1 day, 1 hour, 45 minutes
    """
    weeks, days, hours, minutes = (0, 0, 0, 0)
    fields = uptime.split(",")
    for field in fields:
        if 'week' in field:
            match = re.search(r"(\d+) week", field)
            weeks = int(match.group(1))
        elif 'day' in field:
            match = re.search(r"(\d+) day", field)
            days = int(match.group(1))
        elif 'hour' in field:
            match = re.search(r"(\d+) hour", field)
            hours = int(match.group(1))
        elif 'minute' in field:
            match = re.search(r"(\d+) minute", field)
            minutes = int(match.group(1))
    return (minutes * 60) + (hours * 60 * 60) + (days * 24 * 60 * 60) + (weeks * 7 * 24 * 60 * 60)

def main():
    """
    Integrate your show version functions into the system (for the two Cisco devices).
    In other words, use the database information to make a Netmiko connection.
    From these Netmiko connections retrieve show version and save the vendor, model,
    os_version, serial_number and uptime_seconds to the database.
    """
    django.setup()
    my_devices = NetworkDevice.objects.all()
    print
    for a_device in my_devices:
        if a_device.device_type == 'cisco_ios':
            a_device_netmiko = create_netmiko_dict(a_device)

            # Retrieve show version from device
            remote_conn = ConnectHandler(**a_device_netmiko)
            show_version = remote_conn.send_command_expect("show version")

            # Process show version
            show_ver_obj = NetDeviceInventory(show_version)

            # Save to database
            a_device.vendor = show_ver_obj.vendor
            a_device.model = show_ver_obj.model
            a_device.serial_number = show_ver_obj.serial_number
            a_device.os_version = show_ver_obj.os_version
            uptime = convert_uptime_to_seconds(show_ver_obj.uptime)
            a_device.uptime_seconds = uptime
            a_device.save()

if __name__ == "__main__":
    main()
