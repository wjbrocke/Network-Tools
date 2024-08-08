#!/usr/bin/env python3

from scapy.all import sendp,Ether,ARP,IP,UDP,DHCP,BOOTP,ICMP,TCP
from binascii import unhexlify
import time

if __name__ == "__main__":
    discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=unhexlify("00deadbeef01"), type=0x0800) / IP(src='0.0.0.0', dst='255.255.255.255') / UDP(dport=67,sport=68) / BOOTP(op=1, chaddr=unhexlify("00deadbeef02")) / DHCP(options=[('message-type','discover'), ('end')])

    arp = Ether(dst='ff:ff:ff:ff:ff:ff', src=unhexlify("00deadbeef01"), type=0x0806) / ARP(op='who-has', psrc='192.168.10.10', pdst='192.168.1.1')

    icmp = Ether(dst='00:00:5e:00:01:01', src=unhexlify("00deadbeef01"), type=0x0800) / IP(src='192.168.10.10', dst='192.168.1.1') / ICMP()

    tcp  = Ether(dst='00:00:5e:00:01:01', src=unhexlify("00deadbeef01"), type=0x0800) / IP(src='192.168.10.10', dst='192.168.1.1') / TCP(sport = 55555, dport = 22, flags = 'S')

    for i in range(0,100):
        #sendp(discover, iface="ens2np1", count=10000, verbose=True)
        #sendp(arp, iface="ens2np1", count=10000, verbose=True)
        #time.sleep(1)
        #sendp(arp, iface="ens2np1", count=100, verbose=False)
        ###sendp([discover,arp], iface="ens2np1", count=10000, verbose=True)
        sendp([discover,arp,icmp,tcp], iface="ens2np1", count=10000, verbose=True)
        time.sleep(1)
