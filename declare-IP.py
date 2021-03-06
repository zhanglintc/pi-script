#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import urllib
import fcntl
import struct
import time
import sys, os

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

sleep_time = int(sys.argv[1]) if len(sys.argv) > 1 else 0

if sleep_time:
    print "sleeping"
    time.sleep(sleep_time)

print "sending"

time_now = time.ctime()
# outterIP = urllib.urlopen("http://zhanglintc.work:3322/").read()
outterIP = os.popen('curl -s ip.sb').read().replace("\n", "")
try:
    innerIP = get_ip_address("eth0")
except:
    innerIP = get_ip_address("wlan0")

text = "Raspberry"
desp = "{0}\r\n\r\nPublic: {1}\r\n\r\nPrivate: {2}".format(time_now, outterIP, innerIP)

# use ftqq
# urllib.urlopen("http://sc.ftqq.com/SCU4050Tc966f97aa635c7055d6c8e12444d518c5834fbfd9eaa7.send?text={0}&desp={1}".format(text, desp))

# use wechat
urllib.urlopen("http://zhanglintc.work:8000/send?text=Raspberry Pi:\nPublic: {0}\nPrivate: {1}".format(outterIP, innerIP))



