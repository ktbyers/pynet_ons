#!/usr/bin/env python
from pprint import pprint
import pyeapi

def main():
    pynet_sw1 = pyeapi.connect_to("pynet-sw1")
    output = pynet_sw1.enable("show ip route")

    # Strip off unneeded information
    output = output[0]
    output = output['result']['vrfs']['default']

    # Get the routes
    routes = output['routes']
    print "\n{:>15} {:>15} {:>15}".format("prefix", "interface", "next_hop")
    filler = "-" * 15
    print "{:>15} {:>15} {:>15}".format(filler, filler, filler)
    for prefix, attr in routes.items():
        intf_nexthop = attr['vias'][0]
        interface = intf_nexthop.get('interface', 'N/A')
        next_hop = intf_nexthop.get('nexthopAddr', 'N/A')
        print "{:>15} {:>15} {:>15}".format(prefix, interface, next_hop)
    print

if __name__ == "__main__":
    main()
