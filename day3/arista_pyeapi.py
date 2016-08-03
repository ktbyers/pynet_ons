#!/usr/bin/env python
from pprint import pprint
import pyeapi

pynet_sw1 = pyeapi.connect_to("pynet-sw1")
show_version = pynet_sw1.enable("show version")
pprint(show_version)

