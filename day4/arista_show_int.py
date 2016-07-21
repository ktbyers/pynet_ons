from pprint import pprint
import pyeapi
import sys

pynet_sw1 = pyeapi.connect_to("pynet-sw1")
#try:
#    return_val = pynet_sw1.config(['vlan 901', 'name red'])
#except pyeapi.eapilib.CommandError:
#    pass
#
#print return_val

####pynet_sw1.enable("write memory")
###
###
#show_int = pynet_sw1.enable("show interfaces")
#pprint(show_int)
###sys.exit()
####
#output = pynet_sw1.enable("show vlan")
#output = output[0]['result']['vlans']
#pprint(output)
####
####output = pynet_sw1.enable("show arp")
####pprint(output)
####
###output = pynet_sw1.enable("show ip route")
###pprint(output)
####
#show_run = pynet_sw1.running_config
#print show_run
###
vlan = pynet_sw1.api('vlans')
print vlan.get(1)
print vlan.get(901)
#vlan.create(903)
#pprint(vlan.getall())
####True
###
####print vlan.get(902)
###
####>>> vlan.set_name(902, name='blue')
####True
####>>> vlan.get(902)
####{'state': 'active', 'name': 'blue', 'vlan_id': 902, 'trunk_groups': []}
####>>> quit()
####
####set_state
####set_trunk_groups
###
####intf = pynet_sw1.api('switchports')
