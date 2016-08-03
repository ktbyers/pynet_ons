#!/usr/bin/env python
from ciscoconfparse import CiscoConfParse
import sys

#def main():
if True:
    cisco_file = 'pynet-rtr1.txt'
    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    for c_map in crypto_maps:
        print
        print c_map.text
        for child in c_map.children:
            print child.text
    print

    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',
                                                 childspec=r'pfs group5')
    print "\nCrypto Maps using PFS group5:"
    for entry in crypto_maps:
        print "  {0}".format(entry.text)
    print

    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                                  childspec=r'set peer 5.5.5.1')
    print "\nCrypto maps not peer 5.5.5.1:"
    for entry in crypto_maps:
        print "  {0}".format(entry.text)
    print

#if __name__ == "__main__":
#    main()
