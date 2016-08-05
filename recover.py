from scapy.all import *
import sys

gatewayIp = sys.argv[1]
victimIp = sys.argv[2]
gatewayMac = sys.argv[3]
victimMac = sys.argv[4]

send(ARP(op=2, pdst=gatewayIp, psrc=victimIp, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMac), count=5)
send(ARP(op=2, pdst=victimIp, psrc=gatewayIp, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gatewayMac), count=5)

#python recover.py 192.168.32.254 192.168.32.56 2c:21:72:93:df:00 00:1c:42:69:77:f9
#python recover.py 192.168.32.254 192.168.32.188 2c:21:72:93:df:00 3c:15:c2:e3:56:bc

'''
[*] Network Interface : enp0s5
[*] Gateway IP : 192.168.32.254
[*] Gateway Mac : 2c:21:72:93:df:00
[*] Victim IP : 192.168.32.56
[*] Victim Mac : 00:1c:42:69:77:f9
'''