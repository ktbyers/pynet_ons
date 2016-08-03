#!/usr/bin/env python
import ssl
import jsonrpclib
from pprint import pprint

ssl._create_default_https_context = ssl._create_unverified_context

ip = '184.105.247.72'
port = '443'
username = 'admin1'
password = ''

url = 'https://{}:{}@{}:{}/command-api'.format(username, password, ip, port)

print url
eapi_connect = jsonrpclib.Server(url)
response = eapi_connect.runCmds(1, ['show version'])
pprint(response)

