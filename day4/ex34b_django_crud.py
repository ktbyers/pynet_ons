#!/usr/bin/env python
import django
from net_system.models import NetworkDevice, Credentials

def main():
    django.setup()

    print "\nCreating test_device1 and test_device2."
    test_device1 = NetworkDevice(
        device_name='test_device1',
        device_type='cisco_ios',
        ip_address='1.1.1.70',
        port=22,
    )
    test_device1.save()

    test_device2 = NetworkDevice.objects.get_or_create(
        device_name='test_device2',
        device_type='cisco_ios',
        ip_address='1.1.1.71',
        port=22,
    )

    print "\nSet vendor field for devices."
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        if 'cisco' in a_device.device_type:
            a_device.vendor = 'Cisco'
        elif 'juniper' in a_device.device_type:
            a_device.vendor = 'Juniper'
        elif 'arista' in a_device.device_type:
            a_device.vendor = 'Arista'
        a_device.save()

    for a_device in devices:
        print "- {} > {}".format(a_device, a_device.vendor)

    print "\nDeleting test devices."
    test_device1 = NetworkDevice.objects.get(device_name='test_device1')
    test_device2 = NetworkDevice.objects.get(device_name='test_device2')
    test_device1.delete()
    test_device2.delete()

    print "\nRetrieve object from database using .get()."
    my_device = NetworkDevice.objects.get(device_name='pynet-rtr1')
    print "- {}".format(my_device.device_name)

    print "\nRetrieve all of the objects from the database using the Arista credentials."
    arista_creds = Credentials.objects.all()[1]
    arista_devices = arista_creds.networkdevice_set.all()
    for a_device in arista_devices:
        print "- {} > {}".format(a_device, a_device.vendor)
    print

if __name__ == "__main__":
    main()
