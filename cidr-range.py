#!/usr/bin/env python3

import sys
import ipaddress

if len(sys.argv) < 2:
  print ('Provide an IP address in CIDR format eg. 192.0.2.0/26')
  print ('See:  https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing for more details')

cidr=sys.argv[1]  
iprange = ([str(ip) for ip in ipaddress.IPv4Network(cidr, strict=False)])
ipn=ipaddress.ip_network(cidr, strict=False)

print("%-20s: %s" % ("Start", iprange[0]))
print("%-20s: %s" % ("End", iprange[-1]))
print("%-20s: %s" % ("Num address", ipn.num_addresses))
print("%-20s: %s" % ("Netmask", ipn.netmask))
